from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductForm(forms.Form):
        name=forms.CharField()
        description=forms.CharField()
        price=forms.IntegerField()

class CartForm(forms.Form):
        product=forms.CharField()
        quantity=forms.IntegerField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email= forms.EmailField(max_length=254)
    message = forms.CharField(max_length=255)

class UserEditForm(UserCreationForm):
        email = forms.EmailField(label="Modificar Email")
        password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
        password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
        
        class Meta:
                model= User
                fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
                help_texts = {k:"" for k in fields}


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField()    
    first_name = forms.CharField()    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}