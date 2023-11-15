from rest_framework.serializers import ValidationError
from habits.models import Habit


class RelatedHabitOrRewardValidator:
    """Указание связанной привычки или вознаграждения"""
    def __init__(self, related_habit, reward, pleasant):
        self.related_habit = related_habit
        self.reward = reward
        self.pleasant = pleasant

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        reward = dict(value).get(self.reward)
        pleasant = dict(value).get(self.pleasant)

        if pleasant:
            if related_habit or reward:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')

        else:
            if related_habit is None and reward is None:
                raise ValidationError('Укажите связанную привычку или вознаграждение')

            elif related_habit:
                habit = Habit.objects.get(id=related_habit.id)
                if not habit.is_pleasant:
                    raise ValidationError("Связанная привычка должна быть приятной")

            elif related_habit and reward:
                raise ValidationError('Укажите либо связанную привычку, либо вознаграждение')


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
