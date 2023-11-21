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
    path('hacer_pedido/', core_views.hacer_pedido, name='hacer_pedido'),
    path('administrar_productos/', core_views.administrar_productos, name='administrar_productos'),
    path('administrar_productos/', core_views.administrar_productos, name='administrar_productos'),
    path('crear_producto/', core_views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>/', core_views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', core_views.eliminar_producto, name='eliminar_producto'),
    ]

