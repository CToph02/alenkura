from django.db import models
from coreBD.models import DateTime, Curso, Nivel

# Create your models here.

class StudentParent(DateTime):
    rut = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    ocupation = models.CharField(max_length=20)
    collage_level = models.CharField(max_length=20)
    mail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} {self.lastName}"

class Student(DateTime):
    rut = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=50)
    birthDate = models.CharField(max_length=40)
    bapDiag = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    commune = models.CharField(max_length=40)
    grade = models.CharField(max_length=40)
    etnia = models.CharField(max_length=40, null=True, blank=True)
    fk_parent = models.ForeignKey(StudentParent, on_delete=models.CASCADE)
    fk_curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)
    fk_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.lastName}"