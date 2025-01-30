from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import Parent,Student,LastFace
from django.contrib.auth.decorators import login_required
import os
import cv2
from django.db.models import Q
import winsound
# from playsound import playsound
import face_recognition
import numpy as np




def loginpage(request):
     if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username ")
            return redirect("login")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("login")
        else:

         login(request, user)

        try:
            student_profile = Student.objects.get(user=user)
            return redirect('student',id=student_profile.id)
        except Student.DoesNotExist:
            pass

        try:
            parent_profile = Parent.objects.get(user=user)
            return redirect('parent')
        except Parent.DoesNotExist:
            pass

        return redirect("index")

     return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def student(request,id):
    a=Student.objects.get(id=id)
    return render(request,'student.html',{'student':a})

@login_required(login_url='login')
def parent(request):
    return render(request,'parent.html')



def home(request):
    return render(request,'home.html')