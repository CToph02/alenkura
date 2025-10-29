from django.db import models
from coreBD.models import DateTime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from coreBD.models import Nivel, Curso
    
class UserManager(BaseUserManager):
    def create_user(self, name, rol, email, password=None, **extra_fields):
        from coreBD.models import Rol

        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            rol=rol,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password=None, **extra_fields):
        from coreBD.models import Rol

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(
            email=self.normalize_email(email), 
            name=name,
            password=password,
            **extra_fields
        )

        user.is_admin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin, DateTime):
    from coreBD.models import Rol
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(verbose_name="email address",max_length=150, null=True)

    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_docent = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.name} ({self.rol})"
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

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