from django.db import models
import uuid


class Batch(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    name=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    name=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    ROLE_CHOICES = [
        ('Teacher', 'Teacher'),
        ('H.O.D', 'H.O.D'),
        ('Principal', 'Principal'),
        ('Vice-Principal', 'Vice-Principal'),
    ]
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='static/teacher')
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Teacher',null=True,blank=True)

    def __str__(self):
        return self.name

