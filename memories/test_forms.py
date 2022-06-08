import pytest
from .forms import MemoryForm
from .models import Memory

# Проверка полностью заполненной формы
@pytest.mark.django_db
def test_valid_data(django_user_model):
    user = django_user_model.objects.create_user(username="user1", password="bar")
    form = MemoryForm({
        'owner': user,
        'name': "Moscow",
        'comment': "It is a big city and a capital of Russia",
        'location': "1,1",
    })
    assert True == form.is_valid()

# Проверка не заполненной формы
@pytest.mark.django_db
def test_blank_data():
    form = MemoryForm({
        'owner': "",
        'name': "",
        'comment': "",
        'location': "",
    })
    assert False == form.is_valid()
