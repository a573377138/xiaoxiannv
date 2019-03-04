from django.shortcuts import render
from django.http import HttpResponse
from .models import Actice
from django.utils.timezone import now,localtime
# Create your views here.
def index(request):
    # nown = Actice(datetime=now())
    # nown.save()
    NOW =Actice.objects.get(pk=3)

    print(NOW.datetime)
    return HttpResponse('成功')
