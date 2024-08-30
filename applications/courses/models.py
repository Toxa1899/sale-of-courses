from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models
from applications.product_card.models import ProductCard


# Create your models here.
User = get_user_model()


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
    product_card = models.ForeignKey(ProductCard, on_delete=models.CASCADE, verbose_name="карточка курса")
    lesson_title = models.CharField(max_length=140, verbose_name="название урока")
    lesson_description = models.TextField(verbose_name="описание урока")
    video = models.FileField(upload_to='course/videos', null=True, blank=True, verbose_name='видео урока')
    file = models.FileField(upload_to='course/files', null=True, blank=True, verbose_name='материал курса')
    is_active = models.BooleanField(default=True, verbose_name='активен ли курс')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
