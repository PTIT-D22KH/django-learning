from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user class definition"""
    age = models.PositiveIntegerField(null=True, blank = True)
    job = models.CharField(max_length = 200)
