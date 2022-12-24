from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from reservation.models import Vol,Trajet

# Create your views here.

def hometrajet(request):
    #a="BIENVENUE DANS HOME"
    trajet=Trajet.objects.all()
    vol=Vol.objects.all()
    


    
    
    #a="bonjour"
    #vol=Vol

    # return HttpResponse(trajet)
    return render(request,'hometrajet.html',locals())

def detailtrajet(request,trajet_id):
    trajet=Trajet.objects.get(pk=trajet_id)
    return render(request,'detailtrajet.html',locals())
