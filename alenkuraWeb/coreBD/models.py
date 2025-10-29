from django.db import models

# Create your models here.
class DateTime(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, editable=True)
    updatedAt = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True

class Asignatura(models.Model):
    asignatura = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.asignatura}"

class Rol(models.Model):
    rol = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.rol}"
    
class Nivel(models.Model):
    nivel = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.nivel}"
    
class Curso(models.Model):
    curso = models.CharField(max_length=30)
    fk_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.curso} - {self.fk_nivel}"