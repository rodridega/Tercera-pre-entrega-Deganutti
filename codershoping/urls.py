from django.urls import path
from .views import products, index, cart, contact, create_product, new_cart, product_search,search, delete_product, update_product, ContactList, ContactCreate, ContactDetail, ContactDelete, ContactUpdate, login_request, register, editarPerfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='inicio'),
    path('products/', products, name='productos'),
    path('cart/', cart, name='carrito'),
    path('contact/', contact, name='contacto'),
    path('create-product/', create_product, name="crear_producto"),
    path('new-cart/', new_cart, name='nuevo_carrito'),
    path('product-search/', product_search, name='buscar_producto'),
    path('search/', search, name='resultado_busqueda'),
    path('delete-product/<product_name>/',delete_product , name='eliminar_producto'),
    path('update-product/<product_name>/',update_product , name='editar_producto'),
    path('contact/list/', ContactList.as_view(), name='contact_list'),
    path(r'^(?P<pk>\d+$', ContactDetail.as_view(), name='contact_detail'),
    path(r'^nuevo$', ContactCreate.as_view(), name='contact_create'),
    path(r'^editar$/(?P<pk>\d+)$', ContactUpdate.as_view(), name='contact_update'),
    path(r'^borrar$/(?P<pk>\d+)$', ContactDelete.as_view(), name='contact_delete'),
    path('login/', login_request, name= "login"),
    path('register/', register, name= "register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name= "logout"),
    path('editarPerfil/', editarPerfil, name= "editarPerfil"),

]
