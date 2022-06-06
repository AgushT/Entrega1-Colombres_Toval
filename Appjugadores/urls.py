from django.contrib import admin
from django.urls import path
from Appjugadores.views import antecedentes, estadisticas, inicio, jugadores
#from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio),
    path('jugadores', jugadores),
    path('estadisticas', estadisticas),
    path('antecedentes', antecedentes),
]