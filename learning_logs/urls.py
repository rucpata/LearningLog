"""Definiuje wzorzec adresów URL dla learning_log."""

from django.urls import path

from .views import index, topics

urlpatterns = [
    #Strona główna
    path('', index, name='index'),
    #Strona tematów
    path('topics/', topics, name='topics'),
]