from django import forms 

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision =forms.IntegerField()

class CursoFormulario1(forms.Form):
    nombre = forms.CharField()
    apellido =forms.CharField()

class CursoFormulario2(forms.Form):
    barrio = forms.CharField()
    provincia =forms.IntegerField()