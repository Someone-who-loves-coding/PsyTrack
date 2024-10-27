from django.contrib import admin
from django.urls import path,include
from .views import UserRegistrationView, LoginView
from . import views

urlpatterns = [
    path('', views.landing),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]