from django import forms

class ProductForm(forms.Form):
        name=forms.CharField()
        description=forms.CharField()

class CartForm(forms.Form):
        product=forms.CharField()
        quantity=forms.IntegerField()
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email= forms.EmailField(max_length=254)
    message = forms.CharField(max_length=255)


