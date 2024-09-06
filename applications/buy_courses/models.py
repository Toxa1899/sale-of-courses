from django.contrib.auth import get_user_model
from django.db import models

from applications.product_card.models import ProductCard

# Create your models here.
User = get_user_model()


class BuyCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_buy_courses')
    product_card = models.ForeignKey(ProductCard, on_delete=models.CASCADE, verbose_name='карточка курса',
                                     related_name='product_card_buy_courses')

