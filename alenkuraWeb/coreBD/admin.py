from django.contrib import admin
from .models import Asignatura, Rol, Curso, Nivel
# Register your models here.

admin.site.register(Asignatura)
admin.site.register(Rol)
admin.site.register(Curso)
admin.site.register(Nivel)