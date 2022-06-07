from django.contrib import admin
from django.urls import path
from Appjugadores.views import antecedentes, estadisticas, inicio, jugadores, jugadoresFormulario
#from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio),
    path('jugadores', jugadores, name= 'Jugadores'),
    path('estadisticas', estadisticas, name= 'Estadisticas'),
    path('antecedentes', antecedentes, name= 'Antecedentes'),
    path('jugadoresFormulario', jugadoresFormulario, name= 'JugadoresFormulario'),
]