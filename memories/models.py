from django.db import models
from mapbox_location_field.models import LocationField  
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Memory(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    location = LocationField()

    class Meta:
        verbose_name_plural = 'memories'

    def __str__(self):
        """"Возвращает строковое представление модели"""
        return self.name
