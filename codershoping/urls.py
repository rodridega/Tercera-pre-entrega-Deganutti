from django.urls import path
from .views import products, index, cart, contact, search

urlpatterns = [
    path('', index, name='inicio'),
    path('products/', products, name='productos'),
    path('cart/', cart, name='carrito'),
    path('contact/', contact, name='contacto'),
    path('search/', search, name='buscar'),
]
