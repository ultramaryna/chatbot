from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bot.models import Chat


def index(request):
    #return HttpResponse("BOTTT :*")
    return render(request, 'bot/index.html')

#dodaj chat state
def chat(request):
    user = Chat.objects.create(user_name='TEST2')
    return render(request, 'bot/chat.html',  {'user': user})
