from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from Appjugadores.models import Jugadores, Estadisticas, Antecedentes


class JugadoresFormulario (forms.Form):

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

    nombre_completo= forms.CharField(max_length= 50, widget=forms.TextInput({ "placeholder": "Matias Gutierrez"}))
    fechadenacimiento= forms.DateField(widget=forms.TextInput({ "placeholder": "YYYY-MM-DD"}), label="Fecha de nacimiento") 
    peso=  forms.IntegerField(widget=forms.TextInput({ "placeholder": "50"}))
    altura= forms.IntegerField(widget=forms.TextInput({ "placeholder": "180"}), label="Altura (cm)")
    nacionalidad= forms.ChoiceField(choices=todasLasNacionalidades)


def obtenerJugadoresEnTupla():
    #todasLasEstadisticas = Estadisticas.objects.all()
    todosLosJugadores = Jugadores.objects.all()
    # filter todas los jugadores to return only those that doesn't have estadisticas
    #todosLosJugadores = todosLosJugadores.exclude(nombre_completo__in=todasLasEstadisticas.values_list('jugador', flat=True))
    jugadoresEnTupla = [(jugador.nombre_completo, jugador.nombre_completo) for jugador in todosLosJugadores]
    return jugadoresEnTupla
class EstadisticasFormulario(forms.Form): 
    # En kwargs se envian los argumentos para la función. 
    # Cuando creamos una estadistica, mostramos los jugadores sin estadisticas para que se eliga al mismo
    # Cuando editamos, no queremos que se añadan las opciones con los distintos jugadores
    def __init__(self, *args, **kwargs):
        if not kwargs or not kwargs['initial']['jugador']:
            super(EstadisticasFormulario, self).__init__(*args, **kwargs)
            self.fields['jugador'] = forms.ChoiceField(
                choices=obtenerJugadoresEnTupla() )
        else:
            super(EstadisticasFormulario, self).__init__(*args, **kwargs)
            

    todasLasPosiciones = (
        ("Arquero", "Arquero"),
        ("Defensor", "Defensor"),
        ("Mediocampista", "Mediocampista"),
        ("Delantero", "Delantero"),
    )

    goles=  forms.IntegerField(widget=forms.TextInput({ "placeholder": "30"}))
    velocidad= forms.IntegerField(min_value=0, max_value=10, widget=forms.TextInput({ "placeholder": "1-10"}))
    posicion= forms.ChoiceField(choices=todasLasPosiciones)
    precisiondepase= forms.IntegerField(min_value=0, max_value=10, label="Precisión de pase", widget=forms.TextInput({ "placeholder": "1-10"}))

class AntecedentesFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
        if not kwargs or not kwargs['initial']['jugador']:
            super(AntecedentesFormulario, self).__init__(*args, **kwargs)
            self.fields['jugador'] = forms.ChoiceField(
                choices=obtenerJugadoresEnTupla() )
        else:
            super(AntecedentesFormulario, self).__init__(*args, **kwargs)

    año_de_debut= forms.DateField(widget=forms.TextInput({ "placeholder": "YYYY-MM-DD"}), label="Año de debut") 
    club_debutante= forms.CharField(max_length=50, widget=forms.TextInput({ "placeholder": "Racing"}))
    club_actual= forms.CharField(max_length=50, widget=forms.TextInput({ "placeholder": "Real Madrid"}))

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



