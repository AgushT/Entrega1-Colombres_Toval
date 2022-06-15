from django.contrib import admin
from django.urls import path
from Appjugadores.views import antecedentes, estadisticas, inicio, jugadores, jugadoresFormulario, estadisticasFormulario, antecedentesFormulario, busquedanombre, buscar, leerjugadores


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio),
    path('jugadores', jugadores, name= 'Jugadores'),
    path('jugadores', leerjugadores, name= 'Jugadores'),
    path('estadisticas', estadisticas, name= 'Estadisticas'),
    path('antecedentes', antecedentes, name= 'Antecedentes'),
    path('jugadoresFormulario', jugadoresFormulario, name= 'JugadoresFormulario'),
    path('estadisticasFormulario', estadisticasFormulario, name= 'EstadisticasFormulario'),
    path('antecedentesFormulario', antecedentesFormulario, name= 'AntecedentesFormulario'),
    path('busquedanombre', busquedanombre, name= 'busquedanombre'),
    path('buscar', buscar, name= 'buscar')
]