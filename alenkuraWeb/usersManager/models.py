from django.db import models

class DateTime(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

class User(DateTime):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    active = models.BooleanField()
    fk_rol = models.ForeignKey("Rol", on_delete=models.CASCADE)
    fk_category = models.ForeignKey("UserCategory", on_delete=models.CASCADE)

class UserCategory(DateTime):
    category_id = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name_category}"

class StudentParent(DateTime):
    parent_id = models.AutoField(primary_key=True)
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
    student_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"{self.name} {self.lastName}"