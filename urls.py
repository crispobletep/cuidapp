from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),
    path('registro/', accounts_views.registro, name='registro'),
    path('login/', accounts_views.iniciar_sesion, name='login'),
    path('logout/', accounts_views.cerrar_sesion, name='logout'),
    path('inicio/', core_views.pagina_principal, name='pagina_principal'),
    path('administrar_pedidos/', core_views.administrar_pedidos, name='administrar_pedidos'),
    path('administrar_productos/', core_views.administrar_productos, name='administrar_productos'),
    path('producto/<int:pk>/', core_views.producto_detail, name='producto_detail'),
    path('producto/<int:pk>/edit/', core_views.producto_edit, name='producto_edit'),
    path('producto/<int:pk>/delete/', core_views.producto_delete, name='producto_delete'),
    ]
