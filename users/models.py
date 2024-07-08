from django.db import models

from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model


# User = get_user_model()


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False, default='User')
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_pro = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    pass
    
    
# class BlockedUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)