from django.db import models

# Create your models here.
class DateTime(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

class Asignaturas(models.Model):
    nombre_asignatura = models.CharField(max_length=50)

