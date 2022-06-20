from django.contrib import admin
from django.urls import path
from Appjugadores.views import antecedentes, estadisticas, inicio, jugadores, jugadoresFormulario, estadisticasFormulario, antecedentesFormulario, busquedanombre, buscar, leerjugadores, eliminarjugador, editarJugador, leerEstadisticas, eliminarestadistica, editarEstadistica


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio),
    #path('jugadores', jugadores, name= 'Jugadores'),
    path('jugadores', leerjugadores, name= 'Jugadores'),
    path('estadisticas', leerEstadisticas, name= 'Estadisticas'),
    path('antecedentes', antecedentes, name= 'Antecedentes'),
    path('jugadoresFormulario', jugadoresFormulario, name= 'JugadoresFormulario'),
    path('estadisticasFormulario', estadisticasFormulario, name= 'EstadisticasFormulario'),
    path('antecedentesFormulario', antecedentesFormulario, name= 'AntecedentesFormulario'),
    path('busquedanombre', busquedanombre, name= 'busquedanombre'),
    path('buscar', buscar, name= 'buscar'),
    path('eliminarjugador/<nombre_completo>', eliminarjugador, name= 'eliminarjugador'),
    path('editarjugador/<nombre_completo>', editarJugador, name= 'editarjugador'),
    path('eliminarestadistica/<goles>', eliminarestadistica, name= 'eliminarestadistica'),
    path('editarestadistica/<goles>', editarEstadistica, name= 'editarestadistica'),

]