from rest_framework import serializers

from applications.buy_courses.models import BuyCourse
from applications.courses.models import Course
from applications.product_card.models import ProductCard


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     buy_course = BuyCourse.objects.filter(product_card=instance).first()
    #     return rep

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        validated_data['user'] = user
        product_card_id = validated_data.get('product_card')
        product_card_exists = ProductCard.objects.filter(user=user, id=product_card_id.id).exists()
        if not product_card_exists:
            raise serializers.ValidationError('Вы не можете создать курс по данной карточке')
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        obj_id = self.context['view'].kwargs.get('pk')
        product_card_exists = ProductCard.objects.filter(user=user, id=obj_id).exists()

        if not product_card_exists:
            raise serializers.ValidationError('вы не являетесь создателем данного курса')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


