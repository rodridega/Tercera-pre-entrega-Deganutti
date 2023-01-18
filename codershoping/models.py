from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

class Cart(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()

class Contact(models.Model):
        name = models.CharField(max_length=255)
        email= models.EmailField(max_length=254)
        message = models.CharField(max_length=255)

