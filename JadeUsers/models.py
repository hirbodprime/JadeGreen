from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager




class CustomUserManager(BaseUserManager):
    def create_user(self, username, password,password2 , **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        if password != password2:
            raise ValueError("passwords do not match")
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.set_password(password2)
        user.save()
        return user

    def create_superuser(self, username, password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser): 
    fullname = models.CharField(max_length=150, blank=True)
    password2 = models.CharField(max_length=128) 
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    REQUIRED_FIELDS = ["password2"]