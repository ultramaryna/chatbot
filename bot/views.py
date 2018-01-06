from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bot.models import Chat

def index(request):
    #return HttpResponse("BOTTT :*")
    user = Chat.objects.create(user_name='Joe')
    return render(request, 'bot/index.html',  {'user': user})
