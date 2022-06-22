from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appjugadores.models import Jugadores, Estadisticas, Antecedentes
from Appjugadores.forms import JugadoresFormulario, AntecedentesFormulario, EstadisticasFormulario, UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate




def inicio(self):
    plantilla=loader.get_template ('Appjugadores/inicio.html')
    documento= plantilla.render()
    return HttpResponse(documento)
    


def jugadores(request):
    return render(request, 'Appjugadores/jugadores.html')


def estadisticas(request):
     return render(request, 'Appjugadores/estadisticas.html')



def antecedentes(request):
     return render(request, 'Appjugadores/antecedentes.html')


def jugadoresFormulario(request):    
    if request.method== 'POST':
        miFormulario= JugadoresFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            #nombre_completo= informacion ['nombre_completo']
            #fechadenacimiento= informacion ['fechadenacimiento']
            #altura= informacion ['altura']
            #nacionalidad= informacion ['nacionalidad']
            jugador= Jugadores(nombre_completo= informacion['nombre_completo'], fechadenacimiento= informacion['fechadenacimiento'], peso= informacion['peso'], altura=informacion['altura'], nacionalidad= informacion['nacionalidad'])
            jugador.save()
            return render (request, 'Appjugadores/inicio.html')
    else:
         miFormulario= JugadoresFormulario()
    return render (request, 'Appjugadores/jugadoresFormulario.html', {'miFormulario': miFormulario})

def estadisticasFormulario(request):    
    if request.method== 'POST':
        miFormulario= EstadisticasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
        #goles= informacion ['goles']  
        #velocidad= informacion ['velocidad']
        #posicion= informacion ['posicion']
        #precisiondepase= informacion ['precisiondepase']
            estadistica= Estadisticas(goles= informacion['goles'], velocidad=informacion['velocidad'], posicion= informacion['posicion'], precisiondepase= informacion['precisiondepase'])
            estadistica.save()
            return render (request, 'Appjugadores/inicio.html')
    else:
         miFormulario= EstadisticasFormulario()
    return render (request, 'Appjugadores/estadisticasFormulario.html', {'miFormulario': miFormulario})

def antecedentesFormulario(request):    
    if request.method== 'POST':
        miFormulario= AntecedentesFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
        #año_de_debut= informacion ['año_de_debut']
        #club_debutante= informacion['club_debutante']
        #club_actual= informacion['club_actual']
            antecedentes= Antecedentes(año_de_debut= informacion ['año_de_debut'], club_debutante= informacion ['club_debutante'], club_actual= informacion['club_actual'])
            antecedentes.save()
            return render (request, 'Appjugadores/inicio.html')
    else:
         miFormulario= AntecedentesFormulario()
    return render (request, 'Appjugadores/antecedentesFormulario.html', {'miFormulario': miFormulario})

def busquedanombre(request):
     return render(request, 'Appjugadores/busquedanombre.html')

def buscar(request):
     if request.GET['nombre']:
        
          nombrejugador= request.GET['nombre']
          Jugador= Jugadores.objects.filter(nombre_completo=nombrejugador)
        
          return render (request,'Appjugadores/resultadoBusqueda.html', {'jugador': Jugador[0]})
     else:
          respuesta= "No se ha ingresado el nombre de ningun jugador"
     return HttpResponse(respuesta)

def leerjugadores(request):
  jugadores = Jugadores.objects.all() 
  contexto = {'jugadores': jugadores}
  return render(request, 'Appjugadores/jugadores.html', contexto)

@login_required
def eliminarjugador(request, nombre_completo ):
     jugador= Jugadores.objects.get(nombre_completo= nombre_completo )
     jugador.delete()
     jugadores= Jugadores.objects.all()
     contexto= {'jugadores': jugadores}
     return render(request, "Appjugadores/jugadores.html", contexto)

def editarJugador(request, nombre_completo):  
    jugador= Jugadores.objects.get(nombre_completo= nombre_completo )

    if request.method== 'POST':
        miFormulario= JugadoresFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            jugador.nombre_completo= informacion ['nombre_completo']
            jugador.fechadenacimiento= informacion ['fechadenacimiento']
            jugador.altura= informacion ['altura']
            jugador.nacionalidad= informacion ['nacionalidad']
            #jugador= Jugadores(nombre_completo= informacion['nombre_completo'], fechadenacimiento= informacion['fechadenacimiento'], peso= informacion['peso'], altura=informacion['altura'], nacionalidad= informacion['nacionalidad'])
            jugador.save()
            jugadores= Jugadores.objects.all()
            contexto= {'jugadores': jugadores}
            return render (request, 'Appjugadores/inicio.html', contexto)
    else:
         miFormulario= JugadoresFormulario(initial={'nombre':jugador.nombre_completo, 'fecha de nacimiento':jugador.fechadenacimiento,'peso': jugador.peso,'altura': jugador.altura, 'nacionalidad': jugador.nacionalidad})
         contexto= {'miFormulario': miFormulario, 'nombre_completo': nombre_completo}
    return render (request, 'Appjugadores/editarJugador.html', contexto)

def leerEstadisticas(request):
  estadisticas= Estadisticas.objects.all() 
  contexto = {'estadisticas': estadisticas}
  return render(request, 'Appjugadores/estadisticas.html', contexto)

@login_required
def eliminarestadistica(request, goles ):
     estadistica= Estadisticas.objects.get(goles= goles )
     estadistica.delete()
     estadisticas= Estadisticas.objects.all()
     contexto= {'estadisticas': estadisticas}
     return render(request, "Appjugadores/estadisticas.html", contexto)

def editarEstadistica(request, goles):  
    estadistica= Estadisticas.objects.get(goles= goles )

    if request.method== 'POST':
        miFormulario= EstadisticasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            estadistica.goles= informacion ['goles']  
            estadistica.velocidad= informacion ['velocidad']
            estadistica.posicion= informacion ['posicion']
            estadistica.precisiondepase= informacion ['precisiondepase']
            estadistica.save()
            estadisticas= Estadisticas.objects.all()
            contexto= {'estadisticas': estadisticas}
            return render (request, 'Appjugadores/inicio.html', contexto)
    else:
         miFormulario= EstadisticasFormulario(initial={'goles':estadistica.goles, 'velocidad':estadistica.velocidad,'posicion': estadistica.posicion,'precisiondepase': estadistica.precisiondepase})
         contexto= {'miFormulario': miFormulario, 'goles': goles}
    return render (request, 'Appjugadores/editarEstadistica.html', contexto)

def leerAntecedentes(request):
  antecedentes= Antecedentes.objects.all() 
  contexto = {'antecedentes': antecedentes}
  return render(request, 'Appjugadores/antecedentes.html', contexto)

@login_required
def eliminarantecedente(request, año_de_debut ):
     antecedente= Antecedentes.objects.get(año_de_debut= año_de_debut )
     antecedente.delete()
     antecedentes= Antecedentes.objects.all()
     contexto= {'antecedentes': antecedentes}
     return render(request, "Appjugadores/antecedentes.html", contexto)

def editarAntecedente(request, año_de_debut):  
    antecedente= Antecedentes.objects.get(año_de_debut= año_de_debut )

    if request.method== 'POST':
        miFormulario= AntecedentesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            antecedente.año_de_debut= informacion ['año_de_debut']
            antecedente.club_debutante= informacion['club_debutante']
            antecedente.club_actual= informacion['club_actual']
            antecedente.save()
            antecedentes= Antecedentes.objects.all()
            contexto= {'antecedentes': antecedentes}
            return render (request, 'Appjugadores/inicio.html', contexto)
    else:
         miFormulario= AntecedentesFormulario(initial={'año_de_debut':antecedente.año_de_debut, 'club_debutante': antecedente.club_debutante,'club_actual': antecedente.club_actual})
         contexto= {'miFormulario': miFormulario, 'año_de_debut': año_de_debut}
    return render (request, 'Appjugadores/editarAntecedentes.html', contexto)

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            clave= form.cleaned_data.get('password')
               
            user= authenticate(username=usuario, password= clave)
            if user  is not None:
                login(request, user)  
                return render (request, 'Appjugadores/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render (request, 'Appjugadores/inicio.html', {'mensaje': 'Datos sincorrectos'})
        else:
            return render (request, 'Appjugadores/inicio.html', {'mensaje': 'Error, formulario inválido'})

    else:
        form= AuthenticationForm()
        return render (request, 'Appjugadores/login.html',{'form':form})

def register_request(request):
    if request.method =='POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save() 
            return render (request, 'Appjugadores/inicio.html', {'mensaje':f'Usuario {username} creado :)'})
        else:
               return render (request, 'Appjugadores/inicio.html', {'mensaje':'Error no se pudo crear al usuario'})
               
    else:
        form= UserRegisterForm()
        return render (request, 'Appjugadores/registro.html',{'form':form})

@login_required
def editarPerfil(request):
    usuario= request.user

    if request.method =='POST':
        formulario= UserEditForm(request.POST, instance= usuario)
        if formulario.is_valid():
            informacion =formulario.cleaned_data
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()
            return render(request, 'Appjugadores/inicio.html', { 'mensaje': 'Datos editados con exito'})

    else:
        formulario= UserEditForm(instance=usuario)

        return render(request, "Appjugadores/editarPerfil.html", {"formulario":formulario, "usuario": usuario.username})























