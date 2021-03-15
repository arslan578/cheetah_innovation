from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

USER_TYPES = (
    ('user', 'user'),
    ('client', 'client'),
)


class Users(AbstractUser):
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=24, null=True, blank=True)
    profession = models.CharField(max_length=64, null=True, blank=True)
    pre_define_interests = models.CharField(max_length=64, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    other_interests = models.TextField(blank=True, null=True)
    user_type = models.CharField(max_length=16, choices=USER_TYPES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
