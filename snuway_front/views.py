from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Date

# Create your views here.
def index(request):
    return render(request, 'snuway_front/index.html')

def my(request):
    return render(request, 'snuway_front/my.html')

def lend(request):
    dates = Date.objects.all()
    return render(request, 'snuway_front/lend.html', {'dates': dates})

def lend_list(request):
    return render(request, 'snuway_front/lend_list.html')

def calendar_test(request):
    return render(request, 'snuway_front/calendar_test.html')
