from rest_framework import routers
from .views import UserViewSet
from django.urls import path
from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('register/', views.register_user, name='register'),
]