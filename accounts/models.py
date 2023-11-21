from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CuentaManager(BaseUserManager):
    def create_user(self, usuario, password=None, rol='usuario'):
        if not usuario:
            raise ValueError('El campo usuario es obligatorio')
        user = self.model(
            usuario=self.normalize_email(usuario),
            rol=rol,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password, rol='administrador'):
        user = self.create_user(usuario, password, rol)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Cuenta(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('administrador', 'Administrador'),
        ('usuario', 'Usuario (Cliente)'),
        ('empleado', 'Empleado'),
    )

    usuario = models.CharField(max_length=100, unique=True, default="nombre_default")
    rol = models.CharField(max_length=15, choices=ROLES, default='usuario')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Establece un valor predeterminado para el campo de contraseña
    password = models.CharField(max_length=128, default='')

    objects = CuentaManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['rol']

    def __str__(self):
        return self.usuario

