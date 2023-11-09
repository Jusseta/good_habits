from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=255, verbose_name='имя')
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    chat_id = models.CharField(max_length=20, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'
