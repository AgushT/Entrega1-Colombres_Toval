from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

todasLasNacionalidades = (
    ("Argentino", "Argentino"),
    ("Brasileño", "Brasileño"),
    ("Chileno", "Chileno"),
    ("Colombiano", "Colombiano"),
    ("Costarricense", "Costarricense"),
    ("Cubano", "Cubano"),
    ("Dominicano", "Dominicano"),
    ("Ecuatoriano", "Ecuatoriano"),
    ("Haitiano", "Haitiano"),
    ("Español", "Español")
)
class JugadoresFormulario (forms.Form):
    nombre_completo= forms.CharField(max_length= 50, widget=forms.TextInput({ "placeholder": "Agustín Toval"}))
    fechadenacimiento= forms.DateField(widget=forms.TextInput({ "placeholder": "YYYY-MM-DD"}), label="Fecha de nacimiento") 
    peso=  forms.IntegerField(widget=forms.TextInput({ "placeholder": "50"}))
    altura= forms.IntegerField(widget=forms.TextInput({ "placeholder": "180"}), label="Altura (cm)")
    nacionalidad= forms.ChoiceField(choices=todasLasNacionalidades)


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
    age = forms.IntegerField(label="Edad")
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)

class Meta:
    model= User
    fields= ['username', 'email', 'password1', 'password2']
    help_texts= {k:"" for k in fields}

class UserEditForm (UserCreationForm):
    age = forms.IntegerField(label="Edad")
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Modificar Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)
    
class Meta:
    model= User
    fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    #saca los mensajes de ayuda
    help_texts= {k:"" for k in fields}



