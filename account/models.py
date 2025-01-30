from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    registration_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address=models.TextField(null=True,blank=True)
    present = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media')
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name +' '+self.last_name


class Parent(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.BigIntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face