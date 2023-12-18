from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            phone=89242424242,
            username='User',
            chat_id=449665847,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('1234qwer')
        user.save()
