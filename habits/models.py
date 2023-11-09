from django.db import models
from django.utils import timezone
from users.models import User
from users.models import NULLABLE


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="владелец", **NULLABLE)
    place = models.CharField(max_length=100, verbose_name="место")
    time = models.TimeField(default=timezone.now, verbose_name="время")
    action = models.CharField(max_length=150, verbose_name="действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="признак приятной привычки")
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.PositiveIntegerField(default=24, verbose_name='периодичность в часах')
    reward = models.CharField(max_length=150, verbose_name="вознаграждение", **NULLABLE)
    duration = models.PositiveIntegerField(default=120, verbose_name='время на выполнение в секундах', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f"{self.action}\nВремя: {self.time}\n Место: {self.place}\n"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = 'привычки'
