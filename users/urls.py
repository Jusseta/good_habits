from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserViewSet


app_name = UsersConfig.name

router_user = DefaultRouter()
router_user.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router_user.urls
