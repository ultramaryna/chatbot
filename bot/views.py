# -*- coding: utf-8 -*-
import requests, json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.encoding import python_2_unicode_compatible

# Create your views here.
from django.http import HttpResponse
from bot.models import Chat, User
from .forms import StartForm, MessageForm


def index(request):
    Chat.objects.all().delete() #Usuwa wszytskie messages z bd

    if request.method == 'POST':
        form = StartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            #geo = form.cleaned_data['geo']
            user = User.objects.create(user_name=name)
            return redirect('chat')
    else:
        form = StartForm()

    return render(request, 'bot/index.html', {'form': form})

#dodaj chat state
def chat(request):
    user = User.objects.all().last()
    messages = Chat.objects.all()
    messages_no = Chat.objects.all().count()
    #print(messages)

    #nie działa, wyrzuca mi adres w warszawie :P
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = str(j['latitude'])
    lon = str(j['longitude'])

    #dane z airly - działa, ale powinno być w innym pliku? importy?
    url = "https://airapi.airly.eu/v1/nearestSensor/measurements?latitude="+lat+"&longitude="+lon+"&maxDistance=1000000"
    headers = {'apikey': '1f1a2d1db77740efb5897fc911de0b52'}
    response = requests.get(
        url,
        headers=headers)
    data = response.json()

    # user_name = request.GET.get('name', '')
    # user = Chat.objects.create(user_name=user_name)
    if messages_no == 0:
        message = Chat.objects.create()
        message.bot_welcome(name=user.user_name)
        return redirect('chat')

    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            #decode
            message = Chat.objects.create(message_text=text)
            message.publish()
            response = Chat.objects.create()
            response.bot_respond(text)
            #Chat.objects.all().delete()
            return redirect('chat')

    return render(request, 'bot/chat.html',  {'user': user, 'form': form, 'messages': messages })
