from django.contrib import admin
from django.urls import path
from Appjugadores.views import antecedentes, estadisticas, inicio, jugadores, jugadoresFormulario, creadores, estadisticasFormulario, antecedentesFormulario, busquedanombre, buscar, leerjugadores, eliminarjugador, editarJugador, leerEstadisticas, eliminarestadistica, editarEstadistica, leerAntecedentes, eliminarantecedente, editarAntecedente,  login_request, register_request, editarPerfil #Jugadoreslist, jugadoresDetalles, jugadorCreacion, jugadorEdicion, jugadorEliminacion,
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    #path('jugadores', jugadores, name= 'Jugadores'),
    path('jugadores', leerjugadores, name= 'Jugadores'),
    path('estadisticas', leerEstadisticas, name= 'Estadisticas'),
    path('antecedentes', leerAntecedentes, name= 'Antecedentes'),
    path('jugadoresFormulario', jugadoresFormulario, name= 'JugadoresFormulario'),
    path('estadisticasFormulario', estadisticasFormulario, name= 'EstadisticasFormulario'),
    path('antecedentesFormulario', antecedentesFormulario, name= 'AntecedentesFormulario'),
    path('busquedanombre', busquedanombre, name= 'busquedanombre'),
    path('buscar', buscar, name= 'buscar'),
    path('eliminarjugador/<nombre_completo>', eliminarjugador, name= 'eliminarjugador'),
    path('editarjugador/<nombre_completo>', editarJugador, name= 'editarjugador'),
    path('eliminarestadistica/<id>', eliminarestadistica, name= 'eliminarestadistica'),
    path('editarestadistica/<id>', editarEstadistica, name= 'editarestadistica'),
    path('eliminarantecedente/<id>', eliminarantecedente, name= 'eliminarantecedente'),
    path('editarantecedente/<id>', editarAntecedente, name= 'editarantecedente'),
    #path('jugador/list/', Jugadoreslist.as_view(), name='jugadores_listar'),
    #path('jugador/<pk>', jugadoresDetalles.as_view(), name='jugadores_detalle'),
    #path('jugador/nuevo/', jugadorCreacion.as_view(), name='jugador_crear'),
    #path('jugador/edicion/<pk>', jugadorEdicion.as_view(), name='jugador_editar'),
    #path('jugador/borrar/<pk>', jugadorEliminacion.as_view(), name='jugador_borrar'),
    path('login', login_request, name= 'login'),
    path('register', register_request, name= 'registro'),
    path('logout', LogoutView.as_view(template_name='Appjugadores/logout.html'), name= 'Logout'),
    path('editarPerfil', editarPerfil, name= 'editarPerfil'),
    path("creadores", creadores, name="Creadores"),
]