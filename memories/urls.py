""""Схемы URL для Memories"""

from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'memories'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница для изменения воспоминания
    path('memories/<int:memory_id>/', views.memory, name='memory'),
    # Страница для добавления нового воспоминания
    path('new_memory/', views.new_memory, name='new_memory'),
    # Страница входа
    path("login/", views.login, name="login"),
    # Страница выхода
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    ]