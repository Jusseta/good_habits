from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedHabitOrRewardValidator, DurationValidator, FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedHabitOrRewardValidator(related_habit='related_habit', reward='reward', pleasant='is_pleasant'),
            DurationValidator(field='duration'),
            FrequencyValidator(field='frequency')
        ]
