from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import ProductForm, CartForm, ContactForm, SearchForm
from .models import Product, Cart, Contact

# Create your views here.

def index(request):
    template = loader.get_template("index.html")

    doc = template.render()

    return HttpResponse(doc)

def products(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'products.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CartForm()
    return render(request, 'cart.html', {'form': form})


from django.shortcuts import render


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(name__icontains=query)
            carts = Cart.objects.filter(product__name__icontains=query)
            contacts = Contact.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'products': products, 'carts': carts, 'contacts': contacts})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})
