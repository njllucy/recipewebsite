from django.contrib import admin
from django.urls import path
from . import views
from signup import views
urlpatterns = [
     path('/signup', views.signaction,name='signup'),
]