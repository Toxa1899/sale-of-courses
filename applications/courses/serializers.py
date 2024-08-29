from rest_framework import serializers

from applications.courses.models import Course
from applications.product_card.models import ProductCard


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        validated_data['user'] = user

        product_card_id = validated_data.get('product_card')
        print('----------')
        print(product_card_id)

        product_card_exists = ProductCard.objects.filter(user=user, id=product_card_id.id).exists()

        if not product_card_exists:
            raise serializers.ValidationError('Вы не можете создать курс по данной карточке')

        # Если карточка продукта существует, создаем и возвращаем объект Course
        return Course.objects.create(**validated_data)