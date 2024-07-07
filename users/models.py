from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100, default='User')
    email = models.EmailField(max_length=100, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    