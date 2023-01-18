from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from .forms import ProductForm, CartForm, ContactForm
from .models import Product, Contact, Cart

# Create your views here.

def index(request):
    template = loader.get_template("index.html")

    doc = template.render()

    return HttpResponse(doc)

def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request=request, template_name='products.html', context=context)


def contact(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request=request, template_name='contact.html', context=context)


def cart(request):
    context = {
        'carts': Cart.objects.all()
    }
    return render(request=request, template_name='cart.html', context=context)

def create_product(request):
    if request.method == "POST":
        data = request.POST
        product = Product(name=data['name'], description=data['description'], price=data['price'])
        product.save()
        return render(request, 'products.html')
    else:
        return render(request, template_name='product_form.html')

def new_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            contact = Contact(name=data['name'], email=data['email'], message=data['message'])
            contact.save()
            success = reverse('contacto')
            return render(request=request, template_name='contact_form.html')
        
    else:
        formulario = ContactForm()
        
    return render(request=request, template_name='contact_form.html', context={'formulario': formulario})


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