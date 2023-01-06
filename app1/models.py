from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
class Student(models.Model):
    name = models.CharField(max_length=100)
class Form(models.Model):
    name = models.CharField(max_length=100)
    techer = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    students = models.ManyToManyField(Student)

