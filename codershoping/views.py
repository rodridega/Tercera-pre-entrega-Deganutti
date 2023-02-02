from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProductForm, CartForm, ContactForm, UserEditForm, UserRegisterForm
from .models import Product, Contact, Cart, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    template = loader.get_template("index.html")
    avatares = Avatar.objects.filter(user=request.user.id)

    """ doc = template.render() """
    return render(request, 'index.html', {'url': avatares[0].imagen.url})
    """ return HttpResponse(doc) """

def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request=request, template_name='products.html', context=context)

def create_product(request):
    if request.method == "POST":
        data = request.POST
        product = Product(name=data['name'], description=data['description'], price=data['price'])
        product.save()
        return render(request, 'products.html')
    else:
        return render(request, template_name='product_form.html')

def delete_product(request, product_name):
    product = Product.objects.get(name=product_name)
    product.delete()

    context = {
        'products': Product.objects.all()
    }
    return render(request=request, template_name='products.html', context=context)

def update_product(request, product_name):
    product = Product.objects.get(name=product_name)

    if request.method == "POST":
        data = request.POST
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        
        product.save()
        return render(request=request, template_name='index.html')
    else:
        my_form = ProductForm(initial={'name':product.name,  'description': product.description, 'price':product.price,})
    
    return render(request=request, template_name='update_product.html', context={'my_form': my_form, 'product_name': product_name})



def contact(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request=request, template_name='contact.html', context=context)

class ContactList(ListView):
    model= Contact
    template_name= 'contact_list.html'

class ContactDetail(DetailView):
    model = Contact
    template_name= 'contact_detail.html'

class ContactCreate(CreateView):
    model = Contact
    success_url = 'contact/list'
    fields = ['name', 'email', 'message']

class ContactUpdate(UpdateView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    fields = ['name', 'email', 'message']

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')

def cart(request):
    context = {
        'carts': Cart.objects.all()
    }
    return render(request=request, template_name='cart.html', context=context)


def new_cart(request):
    if request.method == "POST":
        form = CartForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            contact = Cart(product=data['product'],quantity=data['quantity'] )
            contact.save()
            success = reverse('carrito')
            return redirect(success)
        
    else:
        formulario = CartForm()
    return render(request=request, template_name='cart_form.html', context={'formulario': formulario})
        

def product_search(request):
    return render(request=request, template_name='product_search.html')

def search(request):

    if request.GET['name']:
        product = request.GET['name']
        products_result = Product.objects.filter(name__icontains = product)

        return render(request=request, template_name='product_results.html', context={'products': products_result})
    else:
        response = "No enviaste datos"

    return HttpResponse(response)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, 'index.html', {'mensaje':f'Bienvenido {usuario} '})
            else:
                return render(request, 'login.html', {'mensaje': 'Error, datos incorrectos'})
        
        else:
            return render(request, 'login.html', {'mensaje': 'Formulario erroneo'})
    
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:     
        form = UserRegisterForm()     

    return render(request,"register.html" ,  {"form":form})

def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "index.html", {"mensaje": "Usuario editado correctamente!"})

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})
