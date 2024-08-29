from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .tasks import send_activation_code, send_forgot_password_code
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')

        try:
            validate_password(p1)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code.delay(user.email, user.activation_code)
        return user


class ActivateSerializer(serializers.Serializer):
    activation_code = serializers.IntegerField(min_value=1000, required=True)

    class Meta:
        fields = ('activation_code',)


class DeleteAccountSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, required=True, write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_old_password(self, password):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(password):
            raise serializers.ValidationError('Пароль не совпадает с текущим')
        return user



    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')

        try:
            validate_password(p1)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return attrs

    def set_new_password(self):
        request = self.context.get('request')
        user = request.user
        password = self._validated_data.get('new_password')
        user.set_password(password)
        user.save(update_fields=['password'])


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с такой почтой не найден ')
        return email


    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_forgot_password_code.delay(user.email, user.activation_code)


class ForgotPasswordConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    @staticmethod
    def validate_code(code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Неверный код')
        return code

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')

        try:
            validate_password(p1)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return attrs

    def set_new_password(self):
        code = self.validated_data.get('code')
        password = self._validated_data.get('new_password')
        user = User.objects.get(activation_code=code)
        user.set_password(password)
        user.activation_code = ''
        user.save(update_fields=['password', 'activation_code'])


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UpdateUserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, help_text="Upload a new photo.")
    description = serializers.CharField(required=False, help_text="Update your description.")
    link_to_portfolio = serializers.URLField(required=False, help_text="Provide a link to your portfolio.")
    link_to_behance = serializers.URLField(required=False, help_text="Provide a link to your Behance profile.")
    link_to_instagram = serializers.URLField(required=False, help_text="Provide a link to your Instagram profile.")
    link_to_artstation = serializers.URLField(required=False, help_text="Provide a link to your ArtStation profile.")
    first_name = serializers.CharField(required=False, help_text="Provide a firstname")
    last_name = serializers.CharField(required=False, help_text="Provide a lastname")

    class Meta:
        model = User
        fields = ('photo', 'description', 'link_to_portfolio', 'link_to_behance',
                  'link_to_instagram', 'link_to_artstation', 'first_name', 'last_name')

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError({"photo": "Please provide a photo",
                                              "description": "Please provide a description.",
                                              "link_to_portfolio": "Please provide a  portfolio",
                                               "link_to_behance": "Please provide a behance",
                                               "link_to_instagram": "Please provide a instagram",
                                               "link_to_artstation": "Please provide a artstation",
                                               "first_name": "Please provide your first name",
                                               "last_name": "Please provide your last name"})
        return attrs

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


