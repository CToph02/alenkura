from django.db import models

# Create your models here.
class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    active = models.BooleanField()
    fk_rol = models.ForeignKey("Rol", on_delete=models.CASCADE)
    fk_category = models.ForeignKey("Category", on_delete=models.CASCADE)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=20)