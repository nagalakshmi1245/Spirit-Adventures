from django.urls import path
from .views import *

app_name='app1'

urlpatterns = [
    path('',home, name='home'),
    path('getintouch/',getintouch, name='getintouch'),
    path('signup',signupView,name='signup'),
    path('signin',signinView,name='signin'),
    path('goa/',goa, name='goa'),
    path('contact/',contact,name='contact')
]