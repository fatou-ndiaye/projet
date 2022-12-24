from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from reservation.models import Vol,Compagnie
from reservation.forms import CompagnieRegistration

# Create your views here.

def homecompagnie(request):
    #a="BIENVENUE DANS HOME"
    compagnie=Compagnie.objects.all()
    


    
    
    #a="bonjour"
    #vol=Vol

    #return HttpResponse(compagnie)
    return render(request,'homecompagnie.html',locals())

def detailcompagnie(request,compagnie_id):
    compagnie=Compagnie.objects.get(pk=compagnie_id)
    return render(request,'detailcompagnie.html',locals())

def updatecompagnie(request,compagnie_id):
    if request.method == 'POST':
        compagnie=Compagnie.objects.all()
        compagnies=Compagnie.objects.get(pk=compagnie_id)
        mcompagnie=CompagnieRegistration(request.POST,instance=compagnies)
        # fm=CompagnieRegistration(request.POST)
        if mcompagnie.is_valid():
            mcompagnie.save()
            modificationcomp='Vous avez modifier la compagnie ',compagnie_id,' avec succes'
            
            return render(request,'homecompagnie.html',locals())
    else:
        compagnies=Compagnie.objects.get(pk=compagnie_id)
        mcompagnie=CompagnieRegistration(instance=compagnies)
        # fm=CompagnieRegistration(request.POST)
        
        


    return render(request,'updatecompagnie.html',{'form':mcompagnie})    