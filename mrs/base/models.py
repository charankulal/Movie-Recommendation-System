from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True,unique=True)
    recent_liked=models.TextField(null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
