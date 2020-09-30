from django.urls import path, include
#from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from . import views

app_name = 'users'

urlpatterns = [
    # Logowanie
    path('', include('django.contrib.auth.urls'), name='login'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    # rejestracja
    path('register/', views.register, name='register'),
    #wylogowanie
    path('logout/',views.logout_view, name='logout'),
]