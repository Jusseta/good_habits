from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user_create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/', UserListAPIView.as_view(), name='users'),
]

