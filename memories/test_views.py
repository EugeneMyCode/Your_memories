import pytest
import requests

# Проверка главной страницы
def test_main_page():
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200

# Проверка страницы входа
def test_login_page():
    response = requests.get('http://localhost:8000/login/')
    assert response.status_code == 200

# Проверка страницы создания воспоминания
def test_new_memory_page(client, django_user_model):
    user = django_user_model.objects.create_user(username="user1", password="bar")
    client.force_login(user)
    response = client.get('http://localhost:8000/new_memory/')
    assert response.status_code == 200

# Проверка админки
def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200