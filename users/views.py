from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Установка пароля пользователя"""
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()

