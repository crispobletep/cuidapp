from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Otros campos específicos de medicamentos


class Dosis(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    unidad = models.CharField(max_length=50)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dosis = models.ManyToManyField(Dosis, blank=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos de información del cliente


class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    # Otros campos de dirección


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    # Otros campos de información de la sucursal


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    # Otros campos específicos del pedido
