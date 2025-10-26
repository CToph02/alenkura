from django.db import models

# Create your models here.
class Asignaturas(models.Model):
    nombre_asignatura = models.CharField(max_length=50)