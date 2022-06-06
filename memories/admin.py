from django.contrib import admin  
from .models import Memory
from mapbox_location_field.admin import MapAdmin  
  
admin.site.register(Memory, MapAdmin)  
