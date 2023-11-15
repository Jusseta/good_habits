from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     return super(UserSerializer, self).create(validated_data)

    class Meta:
        model = User
        fields = "__all__"
