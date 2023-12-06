from django.contrib import admin
from django.urls import path
from . import views
from base import views
urlpatterns = [
	path('', views.home,name='home'),
    path('/about', views.about,name='about'),
    path('/tags', views.tags,name='tags'),
    path('/recipes', views.recipes,name='recipes'),
    path('/contact', views.contact,name='contact'),
    path('/tagtemplate', views.tagtemplate,name='tagtemplate'),
    path('/singlerecipe', views.singlerecipe,name='singlerecipe'),
    path('/drinks', views.drinks,name='drinks'),
    path('/breakfast', views.breakfast,name='breakfast'),
    path('/lunch', views.lunch,name='lunch'),
    path('/maxican', views.maxican,name='maxican'),
    path('/recipe1', views.recipe1,name='recipe1'),
    path('/recipe2', views.recipe2,name='recipe2'),
    path('/recipe3', views.recipe3,name='recipe3'),
    path('/recipe4', views.recipe4,name='recipe4'),
    path('/recipe5', views.recipe5,name='recipe5'),
]
