from django.contrib import admin
from django.urls import path
from .views import index, resolve
urlpatterns = [
   
    path('<str:urltag>/', resolve, name="resolve"),
    path('', index, name="index"),

]
