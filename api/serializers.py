from rest_framework import serializers
from .models import CustomUser
from accounts.models import Cuenta
from core.models import Pedido, Receta


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'rol', 'is_active', 'is_staff', 'groups', 'user_permissions']


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['id', 'username', 'rol', 'is_active', 'is_staff']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'codigo', 'cliente', 'medicamento', 'dosis', 'fecha_emision', 'estado']

