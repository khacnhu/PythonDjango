from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


# Create your models here.
class Category(models.Model): #courses_category
    name = models.CharField(null=False, unique=True, max_length=255)
    
    def __str__ (selft):
        return selft.name
    
    
class Course(models.Model):
    subject = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False, blank=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)