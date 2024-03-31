from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
