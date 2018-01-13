import requests, json
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

    #geolokalizacja i airly - przenieść do osobnych plików? importy?
    #geolokalizacja
    ip = str(request.META['REMOTE_ADDR'])
    send_url = 'http://freegeoip.net/json/'+ip
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = str(j['latitude'])
    lon = str(j['longitude'])

    #dane z airly
    url = "https://airapi.airly.eu/v1/nearestSensor/measurements?latitude="+lat+"&longitude="+lon+"&maxDistance=1000000"
    headers = {'apikey': '1f1a2d1db77740efb5897fc911de0b52'}
    response = requests.get(
        url,
        headers=headers)
    data = response.json()

    user_name = request.GET.get('name', '')
    user = Chat.objects.create(user_name=user_name)
    form = MessageForm()
    return render(request, 'bot/chat.html',  {'user': user, 'form': form })
