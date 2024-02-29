from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def browseindex(request):
    films=Movie.objects.all()
    context={
        "films":films
    }
    return render(request, 'browse-index.html',context)