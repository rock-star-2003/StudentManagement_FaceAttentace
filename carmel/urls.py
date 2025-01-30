from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('teachers',teachers,name='teachers'),
    path('departments',departments,name='departments'),
    path('contact',contact,name='contact'),
    path('ajax/', ajax, name= 'ajax'),
    path('details/', details, name= 'details'),
    path('scan/',scan,name='scan'),
]