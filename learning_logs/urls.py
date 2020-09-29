"""Definiuje wzorzec adresów URL dla learning_log."""

from django.urls import path

from .views import index, topics, topic, new_topic, new_entry

urlpatterns = [
    #Strona główna
    path('', index, name='index'),
    #Strona tematów
    path('topics/', topics, name='topics'),
    #Strona szczegółowa dotycząca pojedyńczego tematu
    path('topics/<topic_id>', topic, name='topic'),
    #Strona przeznaczona do dodawania nowego tematu
    path('new_topic/', new_topic, name='new_topic'),
    #Strona przeznaczona do dodawania nowego wpisu
    path('new_entry/<topic_id>', new_entry, name='new_entry'),
]