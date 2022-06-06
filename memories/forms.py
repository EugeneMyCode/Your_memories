from django import forms
from .models import Memory

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'comment', 'location']
        labels = {'name': 'Название', 'comment': 'Комментарий', 'location': 'Локация'}