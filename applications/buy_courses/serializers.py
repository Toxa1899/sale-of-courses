from rest_framework import serializers

from applications.buy_courses.models import BuyCourse
from applications.product_card.models import ProductCard


class BuyCourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = BuyCourse
        fields = ['product_card']



    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user

        product_card = validated_data['product_card']
        product_card_price = product_card.price
        print(product_card_price)
        if int(user.rub) < int(product_card_price):
            raise serializers.ValidationError('Недостаточно средств на балансе ')

        user.rub -= product_card_price
        user.save()

        # if user:
        #     raise serializers.ValidationError('Ошибка')
        buy_course = BuyCourse.objects.create(**validated_data)
        return buy_course


