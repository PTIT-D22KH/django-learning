from django.db import models 
from django.contrib.auth.models import User


class Items(models.Model):
    date = models.DateField(null=True)
    description = models.TextField(null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    category = models.CharField(max_length=100)