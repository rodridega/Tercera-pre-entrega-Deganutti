from django import forms
from .models import Product, Cart, Contact

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('product', 'quantity')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
