from django.contrib import admin
from .models import Student,Parent

class StudentAdmin(admin.ModelAdmin):
    list_display=[ 'first_name','gender','phone','email']

admin.site.register(Student,StudentAdmin)

admin.site.register(Parent)