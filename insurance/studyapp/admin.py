from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student
from  .models  import Subject
from .models import  Teacher
admin.site.register(Student)
admin.site.register(Teacher)        
admin.site.register(Subject)