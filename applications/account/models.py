from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.create_activation_code()
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="email")
    photo = models.ImageField(upload_to="media/user", blank=True, null=True, verbose_name="photo")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    link_to_portfolio = models.URLField(blank=True, null=True, verbose_name="link to portfolio")
    link_to_behance = models.URLField(blank=True, null=True, verbose_name="link to behance")
    link_to_instagram = models.URLField(blank=True, null=True, verbose_name="link to instagram")
    link_to_artstation = models.URLField(blank=True, null=True, verbose_name="link to artstation")
    activation_code = models.CharField(max_length=60, blank=True)
    username = None
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        import random
        digits = random.sample("123456789", 4)
        code = ''.join(digits)
        self.activation_code = code



