from django.db import models


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Composicion(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='composiciones')
    ingrediente = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.medicamento.nombre} - {self.ingrediente} - {self.cantidad}"


class Dosis(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.medicamento.nombre} - {self.cantidad} {self.unidad}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    dosis = models.ManyToManyField(Dosis, blank=True)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)  # Campo para la imagen

    def __str__(self):
        return self.medicamento.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, default='')
    # Otros campos de dirección

    def __str__(self):
        return self.direccion


class Receta(models.Model):
    codigo = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.ForeignKey(Dosis, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Receta {self.codigo} - {self.cliente.nombre} - {self.medicamento.nombre}"


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('listo', 'Listo'),
    ]

    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    direccion_cliente = models.ForeignKey(Direccion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Pedido - {self.receta} - {self.get_estado_display()}"
