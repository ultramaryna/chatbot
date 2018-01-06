from django.contrib import admin

# Register your models here.

from .models import Test

admin.site.register(Test)


def index(request):
    lista = Test.objects.all()
    out = ', '.join([q.napis_text for q in lista])
    #return HttpResponse("Blogasek :*")
    #return HttpResponse(lista)
    return HttpResponse(out)
