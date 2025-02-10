from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login


# Create your views here.

def home(request):
    categories = category.objects.prefetch_related('subcategories').all()
    return render(request,'home.html', {'categories': categories})


def getintouch(request):
    if request.method=='POST':
       l=userInfoForm(request.POST)
       if l.is_valid():
           l.save()
    st=userInfoForm()       
    return render(request, 'getintouch.html',{'data':st})



# def basecity(request):
#     f1 = feedbackForm()
#     if request.method == 'POST':
#         f1 = feedbackForm(request.POST)  
#         if f1.is_valid():  
#             f1.save()  
#             return redirect('app1:goa') 
#     F=feedback.objects.all() 
#     return render(request, 'goa.html', {'form': f1,'form1':F})

# def basecitypage(request):
#     city = get_object_or_404(Basecitypage)
#     context = {
#         'city': city, 
#     }
#     return render(request, 'base_cities.html', context)

def cityconnection(request,city_name):
    city = get_object_or_404(Basecitypage, city_name__iexact=city_name)
    package =packages.objects.filter(city=city)
    f1 = feedbackForm()
    if request.method == 'POST':
        f1 = feedbackForm(request.POST)  
        if f1.is_valid():  
            f1.save()  
            return redirect('app1:cityconnection', city_name=city_name) 
    F=feedback.objects.all()  
    return render(request,'base_cities.html',{'city1':city,'packages':package,'form1':F})


def package_details(request, package_id):
    package = get_object_or_404(packages, id=package_id)
    p_categories = package_details_category.objects.prefetch_related('packagedetails').all()  
    return render(request, 'demo.html', {'package': package,'p_categories':p_categories})

@login_required
def Contact(request):
    c1=contactform()
    if request.method=="POST":
        c=contactform(request.POST)
        # b=billingform(request.POST)
        if c.is_valid():
            c.save()
    return render(request,'getintouch.html',{'form':c1})

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


