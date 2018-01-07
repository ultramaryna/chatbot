from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from bot.models import Chat
from .forms import StartForm, MessageForm


def index(request):
    #return HttpResponse("BOTTT :*")
    if request.method == 'POST':
        form = StartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            geo = form.cleaned_data['geo']
    else:
        form = StartForm()

    return render(request, 'bot/index.html', {'form': form})

#dodaj chat state
def chat(request):
    user_name = request.GET.get('name', '')
    user = Chat.objects.create(user_name=user_name)
    form = MessageForm()
    return render(request, 'bot/chat.html',  {'user': user, 'form': form})
