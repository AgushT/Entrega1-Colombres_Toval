from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appjugadores.models import Jugadores, Estadisticas, Antecedentes
from Appjugadores.forms import jugadoresFormulario, antecedentesFormulario, estadisticasFormulario


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
        miFormulario= jugadoresFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
        nombre_completo= informacion ['Nombre Completo']
        fechadenacimiento= informacion ['Fecha de Nacimiento']
        altura= informacion ['Altura']
        nacionalidad= informacion ['Nacionalidad']
        jugador= Jugadores(nombre_completo= nombre_completo, fechadenacimiento= fechadenacimiento, altura= altura, nacionalidad= nacionalidad  )
        jugador.save()
        return render (request, 'Appjugadores/inicio.html')
    else:
         miFormulario= jugadoresFormulario()

    return render (request, 'Appjugadores/profesoresFormulario.html', {'miFormulario': miFormulario})







