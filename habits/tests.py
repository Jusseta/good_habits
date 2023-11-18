from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test11@test.ru',
            password='12qw34er',
            is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place='утром',
            time='10:00:10',
            action='пресс качат',
            is_pleasant=False,
            reward='being healthy',
            frequency=24,
            duration=120,
            is_public=False
        )

    def test_habit_create(self):
        """Тест создания привычки"""
        data = {
            'owner': 1,
            'place': 'утром',
            'time': '11:00',
            'action': 'бегит',
            'is_pleasant': True,
            'frequency': 3,
            'duration': 120,
            'is_public': False
        }

        response = self.client.post(
            '/habits/habit/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        """Тест вывода списка привычек"""
        response = self.client.get('/habits/habit/')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        'id': self.habit.id,
                        'owner': self.user.id,
                        'place': 'утром',
                        'time': '10:00:10',
                        'action': 'пресс качат',
                        'is_pleasant': False,
                        'related_habit': None,
                        'reward': 'being healthy',
                        'frequency': 24,
                        'duration': 120,
                        'is_public': False
                    }
                ]
            }
        )

    def test_habit_detail(self):
        """Тест вывода отдельной привычки"""
        response = self.client.get(f'/habits/habit/{self.habit.id}/')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': self.habit.id,
                'owner': self.user.id,
                'place': 'утром',
                'time': '10:00:10',
                'action': 'пресс качат',
                'is_pleasant': False,
                'related_habit': None,
                'reward': 'being healthy',
                'frequency': 24,
                'duration': 120,
                'is_public': False
            }
        )

    def test_habit_update(self):
        """Тест изменения привычки"""
        data = {
            'action': 'турник',
            'reward': 'анжуманя'
        }
        response = self.client.patch(f'/habits/habit/{self.habit.id}/', data=data)

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': self.habit.id,
                'owner': self.user.id,
                'place': 'утром',
                'time': '10:00:10',
                'action': 'турник',
                'is_pleasant': False,
                'related_habit': None,
                'reward': 'анжуманя',
                'frequency': 24,
                'duration': 120,
                'is_public': False
            }
        )

    def test_lesson_delete(self):
        """Тест удаления привычки"""
        response = self.client.delete(f'/habits/habit/{self.habit.id}/')

        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)

    def test_public_habit_list(self):
        """Тест вывода списка публичных привычек"""
        response = self.client.get('/habits/public_habits/')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 0,
                "next": None,
                "previous": None,
                "results": []
            }
        )

    def test_related_habit_validator(self):
        """Тест валидатора на выбор связанной привычки"""
        data = {
            'related_habit': self.habit.id
        }
        response = self.client.patch(f'/habits/habit/{self.habit.id}/', data=data)

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEquals(
            response.json(),
            {'non_field_errors': ['Связанная привычка должна быть приятной']}
        )
