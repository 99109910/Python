from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    films= Movie.objects.all()
    context={
        "films":films,
    }
    
    
    return render(request,"exxen.html",context)


def Detay(request,filmId):
    films=Movie.objects.filter(id=filmId)
    context={
        "films":films
    }
    
    return render(request,"detail.html",context)

def Olustur(request):
    if request.method=="POST":
        name=request.POST["name"]
        image=request.FILES["image"]
        trial=request.FILES["trial"]
        description=request.POST["description"]
        
        film=Movie.objects.create(
            name=name,image=image,description=description,trial=trial
        )
        film.save()
        return redirect("index")
        
    return render(request,"create.html")