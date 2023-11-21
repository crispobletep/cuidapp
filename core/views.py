from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Cliente
from .forms import PedidoForm, ProductoForm


def pagina_principal(request):
    productos = Producto.objects.all()
    return render(request, 'pagina_principal.html', {'productos': productos})


def hacer_pedido(request, producto_id):
    # Recuperar el producto a partir del ID proporcionado
    producto = Producto.objects.get(pk=producto_id)

    if request.method == 'POST':
        # Procesar el formulario de pedido cuando se envíe
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Crear un nuevo pedido y guardarlo en la base de datos
            pedido = form.save(commit=False)  # No guardar todavía para agregar el producto y el cliente
            pedido.producto = producto  # Asignar el producto al pedido
            pedido.cliente = Cliente.objects.get(id=1)  # Asignar el cliente (debes implementar la lógica real)
            pedido.save()  # Guardar el pedido

            # Redirigir o mostrar una página de confirmación
            return redirect('pedido_confirmado')  # Debes definir esta vista y URL

    else:
        # Mostrar el formulario para hacer el pedido
        form = PedidoForm()

    return render(request, 'hacer_pedido.html', {'producto': producto, 'form': form})


def administrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'administrar_productos.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrar_productos')
    else:
        form = ProductoForm()
    return render(request, 'administrar_productos.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrar_productos')

    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    return redirect('administrar_productos')