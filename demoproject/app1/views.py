from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import *
from .models import *


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
    return render(request,'base_cities.html',{'city1':city,'packages':package})


def package_details(request, package_id):
    package = get_object_or_404(packages, id=package_id)
    p_categories = package_details_category.objects.prefetch_related('packagedetails').all()  
    return render(request, 'demo.html', {'package': package,'p_categories':p_categories})


def Contact(request):
    c1=contactform()
    if request.method=="POST":
        c=contactform(request.POST)
        # b=billingform(request.POST)
        if c.is_valid():
            c.save()
    return render(request,'getintouch.html',{'form':c1})
