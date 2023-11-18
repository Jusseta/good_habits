from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = models.CharField(max_length=255, verbose_name='имя')
    phone = models.CharField(unique=True, max_length=20, verbose_name='телефон')
    chat_id = models.CharField(unique=True, max_length=20, verbose_name='id чата')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'
