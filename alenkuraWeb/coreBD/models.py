from django.db import models

# Create your models here.
class DateTime(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

class Asignaturas(models.Model):
    nombre_asignatura = models.CharField(max_length=50)

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)