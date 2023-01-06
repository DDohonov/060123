from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

site.register(Teacher)
site.register(Form)
site.register(Student)
# Register your models here.
