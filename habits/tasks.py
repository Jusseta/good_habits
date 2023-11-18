import os
import requests
from celery import shared_task
from habits.models import Habit


@shared_task
def send_notification(habit_id):
    """Создание сообщения для отправки в телеграм"""
    habit = Habit.objects.get(id=habit_id)
    message = f'Напоминание!\n' \
              f'{habit.action}\n' \
              f'Место: {habit.place}'
    data = {
        'chat_id': {habit.owner.chat_id},
        'text': message
    }

    r = requests.get(f'https://api.telegram.org/bot{os.getenv("TG_BOT_TOKEN")}/sendMessage', params=data)
    if r.status_code != 200:
        raise Exception(f'sending error {r.status_code}')
    else:
        print('message send')
