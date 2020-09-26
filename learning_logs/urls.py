"""Definiuje wzorzec adresów URL dla learning_log."""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Strona główna
    url(r'^$', views.index),
]