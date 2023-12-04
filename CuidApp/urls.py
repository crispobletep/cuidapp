from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from core import views as core_views
from rest_framework.documentation import include_docs_urls
from core.views import quienes_somos

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
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='Api Documentation')),
    path('marcar_como_listo/<int:pedido_id>/', core_views.marcar_como_listo, name='marcar_como_listo'),
    path('marcar_como_pendiente/<int:pedido_id>/', core_views.marcar_como_pendiente, name='marcar_como_pendiente'),
    path('mis_pedidos/', core_views.mis_pedidos, name='mis_pedidos'),
    ]

