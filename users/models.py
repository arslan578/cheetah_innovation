from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=24, null=True, blank=True)
    profession = models.CharField(max_length=64, null=True, blank=True)
    pre_define_interests = models.CharField(max_length=64, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    other_interests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


