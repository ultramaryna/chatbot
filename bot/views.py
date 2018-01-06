from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bot.models import Chat
from clp3 import clp
import questions

def index(request):
    #return HttpResponse("BOTTT :*")
    user = Chat.objects.create(user_name='TEST2')
    return render(request, 'bot/index.html',  {'user': user})
