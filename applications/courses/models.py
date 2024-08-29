from django.contrib.auth import get_user_model
from django.utils import timezone

from django.db import models

from applications.product_card.models import ProductCard


# Create your models here.
User = get_user_model()

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product_card = models.ForeignKey(ProductCard, on_delete=models.CASCADE, verbose_name="product_card")
    lesson_title = models.CharField(max_length=140)
    lesson_description = models.TextField()
    video = models.FileField(upload_to='course/videos', null=True, blank=True)
    file = models.FileField(upload_to='course/files', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)