from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appjugadores.models import Jugadores, Estadisticas, Antecedentes
from Appjugadores.forms import JugadoresFormulario, AntecedentesFormulario, EstadisticasFormulario


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
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
        #goles= informacion ['goles']  
        #velocidad= informacion ['velocidad']
        #posicion= informacion ['posicion']
        #precisiondepase= informacion ['precisiondepase']
            estadistica= Estadisticas(goles= informacion['goles'], velocidad=['velocidad'], posicion= informacion['posicion'], precisiondepase= informacion['precisiondepase'])
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
     if request.GET['jugador']:
          nombre_completo= request.GET['nombre_completo']
          fechadenacimiento= request.GET['fechadenacimiento']
          peso= request.GET['peso']
          altura= request.GET['altura']
          nacionalidad= request.GET['nacionalidad']
          Jugador= Jugadores.objects.filter(nombre_completo=nombre_completo)
          return render (request,'Appjugadores/resultadoBusqueda.html', {'nombre_completo':nombre_completo, 'fechadenacimiento': fechadenacimiento, 'peso': peso, 'altura': altura, 'nacionalidad': nacionalidad})
     else:
          respuesta= "No se ha ingresado el nombre de ningun jugador"
     return HttpResponse(respuesta)

















