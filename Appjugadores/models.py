from django.db import models

class Jugadores(models.Model):
    nombre_completo = models.CharField(max_length= 50)
    fechadenacimiento= models.DateField() 
    peso=  models.IntegerField()
    altura= models.IntegerField()
    nacionalidad= models.CharField(max_length=30)
    def __str__(self): 
        return self.nombre_completo+ " / "+ self.nacionalidad
    


class Estadisticas(models.Model): 
    jugador= models.CharField(max_length=50, default="")
    goles=  models.IntegerField()
    velocidad= models.IntegerField()
    posicion= models.CharField(max_length=30)
    precisiondepase= models.IntegerField()
    
class Antecedentes(models.Model):
    año_de_debut= models.DateField() 
    club_debutante= models.CharField(max_length=30)
    club_actual= models.CharField(max_length=30)





