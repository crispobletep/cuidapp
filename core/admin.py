from django.contrib import admin
from .models import Medicamento, Producto, Composicion, Categoria, Dosis, Cliente, Direccion, Pedido, Receta

admin.site.register(Medicamento)
admin.site.register(Producto)
admin.site.register(Composicion)
admin.site.register(Categoria)
admin.site.register(Dosis)
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Pedido)
admin.site.register(Receta)
