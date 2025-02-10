from django.urls import path
from .views import *

app_name='app1'

urlpatterns = [
    path('',home, name='home'),
    path('getintouch/',getintouch, name='getintouch'),
    path('signup',signupView,name='signup'),
    path('signin',signinView,name='signin'),
    # path('city/',basecitypage,name='basecitypage'),
    path('city/<str:city_name>/', cityconnection, name='cityconnection'),
    path('package/<int:package_id>/', package_details, name='package_details'),
]
 