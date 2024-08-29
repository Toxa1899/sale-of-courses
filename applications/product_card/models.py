from django.db import models

# Create your models here.


class ProductCard(models.Model):
    cap = models.ImageField(upload_to='product_card/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)


class ProductCardImage(models.Model):
    product = models.ForeignKey(ProductCard, related_name='images', on_delete=models.CASCADE)
    authors_work = models.ImageField(upload_to='product_images/')