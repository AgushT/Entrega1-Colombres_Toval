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
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
        nombre= informacion ['nombre_completo']
        fechadenacimiento= informacion ['fechadenacimiento']
        altura= informacion ['altura']
        nacionalidad= informacion ['nacionalidad']
        jugador= Jugadores(nombre_completo= nombre, fechadenacimiento= fechadenacimiento, altura= altura, nacionalidad= nacionalidad)
        jugador.save()
        return render (request, 'Appjugadores/inicio.html')
    else:
         miFormulario= JugadoresFormulario()
    return render (request, 'Appjugadores/jugadoresFormulario.html', {'miFormulario': miFormulario})













