from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import PublicHabitListAPIView, HabitViewSet


app_name = HabitsConfig.name

router_habit = DefaultRouter()
router_habit.register(r'habit', HabitViewSet, basename='habit')


urlpatterns = [
    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits'),

] + router_habit.urls



