from datetime import datetime, timedelta
from django_celery_beat.models import IntervalSchedule, PeriodicTask


def create_schedule(frequency, action):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=frequency,
        period=IntervalSchedule.HOURS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name=action,
        task='habits.tasks.send_notification',
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
