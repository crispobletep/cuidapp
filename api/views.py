from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from accounts.models import Cuenta
from .serializers import CuentaSerializer


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CuentaListCreateView(generics.ListCreateAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer


class CuentaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
