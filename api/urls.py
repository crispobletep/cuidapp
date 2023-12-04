from django.urls import path
from .views import CustomUserListCreateView, CustomUserDetailView
from .views import CuentaListCreateView, CuentaDetailView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('cuentas/', CuentaListCreateView.as_view(), name='cuenta-list'),
    path('cuentas/<int:pk>/', CuentaDetailView.as_view(), name='cuenta-detail'),
]


