from django.contrib import admin
from django.urls import path
from . import views
from login import views
urlpatterns = [
     path('/login', views.loginaction,name='login'),
    path('/error', views.error,name='error'),
    path('/welcome',views.welcome,name='welcome'),
]