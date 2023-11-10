from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedHabitOrRewardValidator, DurationValidator, RelatedHabitValidator, \
    IsPleasantHabitValidator, FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedHabitOrRewardValidator(related_habit='related_habit', reward='reward'),
            DurationValidator(field='duration'),
            RelatedHabitValidator(field='related_habit'),
            IsPleasantHabitValidator(field='is_pleasant'),
            FrequencyValidator(field='frequency')
        ]
