from rest_framework.serializers import ValidationError
from habits.models import Habit


class RelatedHabitOrRewardValidator:
    """Исключение одновременного выборф связанной привычки и указания вознаграждения"""
    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        reward = dict(value).get(self.reward)
        if related_habit and reward:
            raise ValidationError('Укажите либо связанную привычку, либо вознаграждение')
        elif related_habit is None and reward is None:
            raise ValidationError('Укажите связанную привычку или вознаграждение')


class DurationValidator:
    """Ограничение времени выполнения привычки"""
    def __init__(self, field):
        self.duration = field

    def __call__(self, value):
        duration = dict(value).get(self.duration)
        if duration is None:
            duration = 120
        if duration > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class RelatedHabitValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""
    def __init__(self, field):
        self.related_habit = field

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        if related_habit is not None:
            habit = Habit.objects.get(id=related_habit.id)
            if not habit.is_pleasant:
                raise ValidationError("Выбранная привычка не приятная")


class IsPleasantHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""
    def __init__(self, field):
        self.is_pleasant = field

    def __call__(self, value):
        is_pleasant = dict(value).get(self.is_pleasant)
        if is_pleasant:
            related_habit = value.get('related_habit')
            reward = value.get('reward')
            if related_habit is not None or reward is not None:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class FrequencyValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""
    def __init__(self, field):
        self.frequency = field

    def __call__(self, value):
        frequency = dict(value).get(self.frequency)
        if frequency is None:
            frequency = 24

        if frequency > 168:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


