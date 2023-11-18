from datetime import datetime, timedelta
from django_celery_beat.models import IntervalSchedule, PeriodicTask


def create_schedule(habit):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.frequency,
        period=IntervalSchedule.HOURS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name=f'{habit.action} в {habit.time}',
        task='habits.tasks.send_notification',
        args=[habit.id]
    )
