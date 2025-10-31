from django import forms
from coreBD.models import Curso, Nivel, Rol

class DocenteForm(forms.Form):
    name = forms.CharField(label="Nombre")
    email = forms.CharField(label="Correo")
    password = forms.CharField(label="Contraseña")
    curso = forms.CharField(label="Curso")
    level = forms.CharField(label="Nivel")
    rol = forms.CharField(label="Nivel")