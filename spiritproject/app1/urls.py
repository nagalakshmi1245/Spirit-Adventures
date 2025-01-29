from django.urls import path
from .views import *

app_name='app1'

urlpatterns = [
    path('',home, name='home'),
    path('getintouch/',getintouch, name='getintouch'),
    
    path('goa/',goa, name='goa'),
    path('pondicherry/',pondicherry, name='pondicherry'),
    path('vizag/',vizag, name='vizag'),
    
    path('manali/',manali, name='manali'),
    path('himalayas/',himalayas, name='himalayas'),
    path('coorg/',coorg, name='coorg'),
    path('meghalaya/',meghalaya, name='meghalaya'),
    
    path('ooty/',ooty, name='ooty'),
    path('munnar/',munnar, name='munnar'),
    path('shimla/',shimla, name='shimla'),
    path('darjeeling/',darjeeling, name='darjeeling'),
    
    path('tirupati/',tirupati, name='tirupati'),
    path('ayodhya/',ayodhya, name='ayodhya'),
    path('varanasi/',varanasi, name='varanasi'),
    path('shirdi/',shirdi, name='shirdi'),
    path('kedarnath/',kedarnath, name='kedarnath'),
    
    path('delhi/',delhi, name='delhi'),
    path('mysore/',mysore, name='mysore'),
    path('agra/',agra, name='agra'),
    path('hyderabad/',hyderabad, name='hyderabad'),
    path('contact/',contact,name='contact')
]