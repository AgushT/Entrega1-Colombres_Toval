from django.contrib import admin

from Appjugadores.models import Antecedentes, Estadisticas, Jugadores

# Register your models here.
admin.site.register(Jugadores)

admin.site.register(Antecedentes)

admin.site.register(Estadisticas)