from django import forms
from .models import Contacto,Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError




class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=['nombre','correo','tipo_consulta','mensaje','avisos']

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3 , max_length=50)
    imagen=forms.ImageField(required=False,validators=[MaxSizeFileValidator(max_file_size=2)])
    precio=forms.IntegerField(min_value=1)

    class Meta:
        model=Producto
        fields='__all__'

        widgets={
            
            'fecha_fabricacion': forms.SelectDateWidget
        }        

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']