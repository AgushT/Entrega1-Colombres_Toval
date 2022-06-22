from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class JugadoresFormulario (forms.Form):
    nombre_completo= forms.CharField(max_length= 50)
    fechadenacimiento= forms.DateField() 
    peso=  forms.IntegerField()
    altura= forms.IntegerField()
    nacionalidad= forms.CharField(max_length=30)


class EstadisticasFormulario(forms.Form): 
    goles=  forms.IntegerField()
    velocidad= forms.IntegerField()
    posicion= forms.CharField(max_length=30)
    precisiondepase= forms.IntegerField()

class AntecedentesFormulario(forms.Form):
    año_de_debut= forms.DateField() 
    club_debutante= forms.CharField(max_length=30)
    club_actual= forms.CharField(max_length=30)

class UserRegisterForm (UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)

class Meta:
    model= User
    fields= ['username', 'email', 'password1', 'password2']
    help_texts= {k:"" for k in fields}

class UserEditForm (UserCreationForm):
    last_name= forms.CharField(label='Modificar el Apellido')
    first_name= forms.CharField(label='Modificar el Nombre')
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Modificar Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)
    
class Meta:
    model= User
    fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    #saca los mensajes de ayuda
    help_texts= {k:"" for k in fields}



