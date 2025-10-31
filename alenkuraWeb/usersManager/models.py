from django.db import models
from coreBD.models import DateTime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from coreBD.models import Nivel, Curso
    
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
        extra_fields.setdefault('is_admin', True)

        admin_rol, created = Rol.objects.get_or_create(rol='Admin')

        user = self.create_user(
            email=self.normalize_email(email), 
            name=name,
            password=password,
            rol=admin_rol,
            **extra_fields
        )

        user.is_admin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin, DateTime):
    from coreBD.models import Rol
    name = models.CharField(max_length=100)
    email = models.CharField(verbose_name="email address",max_length=150, unique=True)

    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_docent = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name} ({self.rol})"
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
