import os
from datetime import datetime
import requests
from celery import shared_task
from habits.models import Habit


@shared_task
def send_notification():
    """Создание сообщения для отправки в телеграм"""
    current_time = datetime.now().time()
    habits = Habit.objects.filter(time=current_time)
    url = f'https://api.telegram.org/bot{os.getenv("TG_BOT_TOKEN")}/sendMessage'

    for habit in habits:
        if habit.time >= current_time:
            message = f'Напоминание!\n' \
                      f'{habit.action}\n' \
                      f'Место: {habit.place}'

            data = {
                'chat_id': {habit.owner.chat_id},
                'text': message
            }

            r = requests.post(url, data=data)

            if r.status_code != 200:
                raise Exception(f'sending error {r.status_code}')
            else:
                print('message send')


            # print(requests.get(url).json())