from django.db import models
from django import forms 
from django.utils import timezone
from django.contrib.auth.models import User

class kursi(models.Model):
    id = models.AutoField(primary_key=True)
    titulli = models.CharField(max_length=100)
    moduli = models.CharField(max_length=100)
    permbajtja = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


class njoftimet(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name =  models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=300, null=True)
    content= models.TextField()
    document = models.FileField(upload_to='uploads', null=True)
    url = models.CharField(max_length=1000, null=True)
    
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title


