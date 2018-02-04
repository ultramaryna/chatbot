# -*- coding: utf-8 -*-
import requests, json, ast
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.encoding import python_2_unicode_compatible

# Create your views here.
from django.http import HttpResponse
from bot.models import Chat, User
from .forms import StartForm, MessageForm
from .data import *


def index(request):
    Chat.objects.all().delete() #Usuwa wszytskie messages z bd

    if request.method == 'POST':
        form = StartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            geo = form.cleaned_data['geo']
            if geo:
                ip = str(request.META['REMOTE_ADDR'])
                user_geolocation = get_geolocation(ip)
                lat = user_geolocation['lat']
                lon = user_geolocation['lon']
            else:
                lat = ''
                lon = ''
            user = User.objects.create(user_name=name, user_lat=lat, user_lon=lon)
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
    message_weather = ''

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
            text = str(text)
            message = Chat.objects.create(message_text=text)
            message.publish()
            response = Chat.objects.create()
            response.bot_respond(text, name=user.user_name, lat=user.user_lat, lon=user.user_lon)
            last_message = str(Chat.objects.all().last())
            if last_message[0] == '{':
                message_weather = ast.literal_eval(last_message)
                print('lalalalal')
                print(type(message_weather))
                print(message_weather)


            #Chat.objects.all().delete()
            return redirect('chat')

    return render(request, 'bot/chat.html',  {'user': user, 'form': form, 'messages': messages, 'message_weather':message_weather })
