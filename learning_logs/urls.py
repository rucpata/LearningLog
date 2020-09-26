"""Definiuje wzorzec adresów URL dla learning_log."""

from django.urls import path

from .views import index

urlpatterns = [
    #Strona główna
    path('', index, name='index'),
]