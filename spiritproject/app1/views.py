from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def home(request):
    categories = category.objects.prefetch_related('subcategories').all()
    return render(request, 'home.html', {'categories': categories})

def getintouch(request):
    if request.method=='POST':
       l=userInfoForm(request.POST)
       if l.is_valid():
           l.save()
    st=userInfoForm()       
    return render(request, 'getintouch.html',{'data':st})



def goa(request):
    f1 = feedbackForm()
    if request.method == 'POST':
        f1 = feedbackForm(request.POST)  
        if f1.is_valid():  
            f1.save()  
            return redirect('app1:goa') 
    F=feedback.objects.all() 
    return render(request, 'goa.html', {'form': f1,'form1':F})





def contact(request):
    c1=contactform()
    if request.method=="POST":
        c=contactform(request.POST)
        # b=billingform(request.POST)
        if c.is_valid():
            c.save()
    return render(request,'contact.html',{'form':c1})

def signupView(request):
    if request.method=='POST':
        s=signupform(request.POST)
        if s.is_valid():
            s.save()
            return redirect('app1:signin')
    return render(request,'signup.html',{'form':signupform()})

def signinView(request):
    f1=signinform()
    if request.method=="POST":
        form=signinform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('app1:contact')
            else:
                return HttpResponse('invalid username and password')
    return render(request,'signup.html',{'form':f1})

def logoutView(request):
    logout(request)
    return redirect('app1:signin')

