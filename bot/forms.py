from django import forms
from .models import Chat

class StartForm(forms.Form):
    name = forms.CharField(label='Twoje imię', max_length=100)
    geo = forms.BooleanField(label='Wyrażam zgodę na udostępnienie swojej lokalizacji.', required=False)

class MessageForm(forms.Form):
    text = forms.CharField(label="Wiadomość", max_length=5000)
