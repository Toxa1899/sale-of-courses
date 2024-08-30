from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
# Create your models here.
User = get_user_model()

class ProductCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cap = models.ImageField(upload_to='product_card/', verbose_name='шапка курса')
    name = models.CharField(max_length=100, verbose_name="название курса")
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='цена курса')
    is_active = models.BooleanField(default=True, verbose_name='активна ли карточка')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



class ProductCardImage(models.Model):
    product = models.ForeignKey(ProductCard, related_name='productcardimage_set', on_delete=models.CASCADE)
    authors_work = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
