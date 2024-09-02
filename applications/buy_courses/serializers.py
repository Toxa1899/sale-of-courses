from rest_framework import serializers

from applications.buy_courses.models import BuyCourse
from applications.product_card.models import ProductCard
from applications.product_card.serializers import ProductCardSerializer


class BuyCourseSerializer(serializers.ModelSerializer):
    product_card = ProductCardSerializer()

    class Meta:
        model = BuyCourse
        fields = ['product_card']


class BuyCoursePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyCourse
        fields = ['product_card']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user

        product_card = validated_data['product_card']
        product_card_price = product_card.price


        if int(user.rub) < int(product_card_price):
            raise serializers.ValidationError('Недостаточно средств на балансе ')

        if ProductCard.objects.filter(user=user, id=product_card.id).exists():
            raise serializers.ValidationError("Вы не можете приобрести собственный курс")

        if BuyCourse.objects.filter(user=user, product_card=product_card).exists():
            raise serializers.ValidationError('Вы уже приобрели данный курс')

        user.rub -= int(product_card_price)
        product_card = ProductCard.objects.get(id=product_card.id)
        product_card_user = product_card.user
        product_card_user.rub += product_card_price

        product_card_user.save()
        user.save()
        buy_course = BuyCourse.objects.create(**validated_data)
        return buy_course



class BuyCoursesInfoSerializer(serializers.ModelSerializer):
    product_card = ProductCardSerializer()
    class Meta:
        model = BuyCourse
        fields = ["product_card"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep