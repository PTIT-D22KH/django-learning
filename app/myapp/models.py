from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()


class Offers(models.Model):
    code = models.CharField(max_length=10)
    product_name = models.CharField(max_length=255)
    discount = models.FloatField()


class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.BooleanField()