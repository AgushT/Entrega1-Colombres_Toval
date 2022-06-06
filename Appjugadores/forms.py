from django import forms


class jugadoresFormulario (forms.Form):
    nombre_completo = forms.CharField(max_length= 50)
    fechadenacimiento= forms.DateField() 
    peso=  forms.IntegerField()
    altura= forms.IntegerField()
    nacionalidad= forms.CharField(max_length=30)


class estadisticasFormulario(forms.Form): 
    goles=  forms.IntegerField()
    velocidad= forms.IntegerField()
    posicion= forms.CharField(max_length=30)
    precisiondepase= forms.IntegerField()

class antecedentesFormulario(forms.Form):
    año_de_debut= forms.DateField() 
    club_debutante= forms.CharField(max_length=30)
    club_actual= forms.CharField(max_length=30)
