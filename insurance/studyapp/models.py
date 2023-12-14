# yourappname/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=2)
   

    def __str__(self):
        return self.name




class   Teacher(models.Model):
    name   =    models.CharField(max_length=205)
    age =   models.IntegerField()
    subject =   models.CharField(max_length=100)
    


class  Subject(models.Model):
    name = models.CharField(max_length=100)
    enrolledStudents   =  models.IntegerField(default=0)
