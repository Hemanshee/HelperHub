from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('user','User'),
        ('helper','Helper')
    )
    user_type = models.CharField(max_length=20,choices=USER_TYPE_CHOICES)