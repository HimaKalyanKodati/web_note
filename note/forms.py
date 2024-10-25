from django import forms
from .models import Note

class dataForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
