from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *

# Create your views here.

def home(request):
    categories = category.objects.prefetch_related('subcategories').all()
    return render(request, 'home.html', {'categories': categories})

def getintouch(request):
    return render(request, 'getintouch.html')


def goa(request):
    f1 = feedbackForm()
    if request.method == 'POST':
        f1 = feedbackForm(request.POST)  
        if f1.is_valid():  
            f1.save()  
            return redirect('app1:goa') 
    F=feedback.objects.all() 
    return render(request, 'goa.html', {'form': f1,'form1':F})



def pondicherry(request):
    return render(request,'pondicherry.html')
def vizag(request):
    return render(request,'vizag.html')



def manali(request):
    return render(request,'manali.html')
def himalayas(request):
    return render(request,'himalayas.html')
def coorg(request):
    return render(request,'coorg.html')
def meghalaya(request):
    return render(request,'meghalaya.html')



def ooty(request):
    return render(request,'ooty.html')
def munnar(request):
    return render(request,'munnar.html')
def shimla(request):
    return render(request,'shimla.html')
def darjeeling(request):
    return render(request,'darjeeling.html')



def tirupati(request):
    return render(request,'tirupati.html')
def ayodhya(request):
    return render(request,'ayodhya.html')
def varanasi(request):
    return render(request,'varanasi.html')
def shirdi(request):
    return render(request,'shirdi.html')
def kedarnath(request):
    return render(request,'kedarnath.html')



def delhi(request):
    return render(request,'delhi.html')
def mysore(request):
    return render(request,'mysore.html')
def agra(request):
    return render(request,'agra.html')
def hyderabad(request):
    return render(request,'hyderabad.html')


def contact(request):
    c1=contactform()
    if request.method=="POST":
        c=contactform(request.POST)
        # b=billingform(request.POST)
        if c.is_valid():
            c.save()
    return render(request,'contact.html',{'form':c1})