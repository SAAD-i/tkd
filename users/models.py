from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings



class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False, default='User')
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_pro = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
class BlockedUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)