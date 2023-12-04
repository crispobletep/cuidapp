from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CuentaManager(BaseUserManager):
    def create_user(self, username, password=None, rol='usuario'):
        if not username:
            raise ValueError('El campo username es obligatorio')

        user = self.model(
            username=username,
            rol=rol
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, rol='administrador'):
        user = self.create_user(username, password, rol)
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

    username = models.CharField(max_length=100, unique=True, default='')  # Cambiado de 'usuario' a 'username'
    rol = models.CharField(max_length=15, choices=ROLES, default='usuario')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CuentaManager()

    USERNAME_FIELD = 'username'  # Cambiado de 'usuario' a 'username'
    REQUIRED_FIELDS = ['rol']

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return self.username

