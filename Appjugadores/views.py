from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appjugadores.models import jugadores, estadisticas, antecedentes


def inicio(self):
    plantilla= loader.get_template('Appjugadores/inicio.html')
    documento= plantilla.render()
    return HttpResponse(documento)


def jugadores(request):
    #documento= "Pagina de cursos"
    return render(request, 'Appjugadodes/jugadores.html')


def estadisticas(request):
     return render(request, 'Appjugadores/estadisticas.html')



def antecedentes(request):
     return render(request, 'Appjugadores/antecedentes.html')






