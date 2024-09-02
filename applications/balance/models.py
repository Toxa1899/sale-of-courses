import uuid

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance_user', blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    link_uuid = models.UUIDField(default=uuid.uuid4, blank=True, null=True)
    payment = models.BooleanField(default=False, verbose_name='Оплачено ли')