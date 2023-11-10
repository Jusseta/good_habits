from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """Вьюсет привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPaginator

    def perform_create(self, serializer):
        """Запись владельца привычки"""
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()

    def get_queryset(self):
        """Вывод привычек данного пользователя"""
        queryset = Habit.objects.filter(owner=self.request.user)
        return queryset


class PublicHabitListAPIView(generics.ListAPIView):
    """Список публичных привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Вывод привычек, у которых положительный признак публичности"""
        queryset = Habit.objects.filter(is_public=True)
        return queryset
