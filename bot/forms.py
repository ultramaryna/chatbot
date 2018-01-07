from django import forms
from .models import Chat

class StartForm(forms.Form):
    name = forms.CharField(label='Twoje imię', max_length=100)
    geo = forms.BooleanField(required=False)
    