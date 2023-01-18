from django.urls import path
from .views import products, index, cart, contact, create_product, new_contact, new_cart, product_search,search

urlpatterns = [
    path('', index, name='inicio'),
    path('products/', products, name='productos'),
    path('cart/', cart, name='carrito'),
    path('contact/', contact, name='contacto'),
    path('create-product/', create_product, name="crear_producto"),
    path('new-contact/', new_contact, name='nuevo_contacto'),
    path('new-cart/', new_cart, name='nuevo_carrito'),
    path('product-search/', product_search, name='buscar_producto'),
    path('search/', search, name='resultado_busqueda')

]
