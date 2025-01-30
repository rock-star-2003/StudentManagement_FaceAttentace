from django.urls import path
from .views import  *

urlpatterns = [
    path('login',loginpage,name='login'),
    path('logout/', logout_page, name='logout'),
    path('student/<int:id>',student,name='student'),
    path('parent',parent,name='parent'),

    

    path('home/', home, name= 'home'),

]