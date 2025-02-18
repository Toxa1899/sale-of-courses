from rest_framework import serializers
from .models import ProductCard, ProductCardImage


class ProductCardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCardImage
        fields = ('id', 'authors_work')






class ProductCardSerializer(serializers.ModelSerializer):



    class Meta:
        model = ProductCard
        fields = ('id', 'name', 'authors_work', 'images_data', 'price', 'cap', 'description', 'is_active', 'sales', 'money_sales')


    authors_work = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True
    )

    images_data = ProductCardImageSerializer(many=True, read_only=True, source='productcardimage_set')

    sales = serializers.SerializerMethodField()
    money_sales = serializers.SerializerMethodField()



    def get_sales(self, obj):

        return getattr(obj, 'sales', None)

    def get_money_sales(self, obj):
        return getattr(obj, 'money_sales', None)


    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        images = validated_data.pop('authors_work', [])

        product = super().create(validated_data)
        for image in images:
            ProductCardImage.objects.create(product=product, authors_work=image)
        return product