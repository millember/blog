from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель для пользователей
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    phone = models.CharField(max_length=35, verbose_name="телефон", help_text="Введите номер телефона", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", help_text="Загрузите свой аватар", **NULLABLE)
    country = models.CharField(max_length=20, verbose_name="страна", help_text="Введите свою страну", **NULLABLE)

    token = models.CharField(max_length=100, verbose_name="токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
