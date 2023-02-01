from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    def __str__(self):
        return f"Producto: {self.name} - Precio: {self.price} - Descripcion: {self.description}"

class Cart(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    def __str__(self):
        return f"Productos en el carrito: {self.product} - Cantidad: {self.quantity}"

class Contact(models.Model):
        name = models.CharField(max_length=255)
        email= models.EmailField(max_length=254)
        message = models.CharField(max_length=255)
        def __str__(self):
            return f"Contacto: {self.name} - Email: {self.email} - Mensaje: {self.message}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"