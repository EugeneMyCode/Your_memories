import pytest
from .models import Memory

# Проверка создания впечатления
@pytest.mark.django_db
def test_memory_create(django_user_model):
   user = django_user_model.objects.create(username='joe', password="something")
   memory = Memory.objects.create(
      name="Siberia",
      comment="I was born there. It's very cold place",
      owner= user
   )
   assert memory.name == "Siberia"
   assert memory.comment == "I was born there. It's very cold place"