"""Definiuje wzorzec adresów URL dla learning_log."""

from django.urls import path

from .views import index, topics, topic

urlpatterns = [
    #Strona główna
    path('', index, name='index'),
    #Strona tematów
    path('topics/', topics, name='topics'),
    #Strona szczegółowa dotycząca pojedyńczego tematu
    path('topics/<topic_id>', topic, name='topic'),
]