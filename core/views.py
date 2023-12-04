from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido, Receta
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def pagina_principal(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='administrador').exists():
            return redirect('administrar_productos')
        elif request.user.groups.filter(name='empleado').exists():
            return redirect('administrar_pedidos')

    productos = Producto.objects.all()
    return render(request, 'pagina_principal.html', {'productos': productos})


def administrar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'administrar_pedidos.html', {'pedidos': pedidos})


def administrar_productos(request):
    productos = Producto.objects.all()
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administrar_productos')

    return render(request, 'administrar_productos.html', {'productos': productos, 'form': form})


def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})


def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(instance=producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrar_productos')

    return render(request, 'producto_form.html', {'form': form, 'edit': True})


def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('administrar_productos')


def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def marcar_como_listo(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.estado = 'listo'
    pedido.save()
    return JsonResponse({'message': 'Pedido listo'})


def marcar_como_pendiente(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.estado = 'pendiente'
    pedido.save()
    return JsonResponse({'message': 'Pedido pendiente'})


def mis_pedidos(request):
    # Asegúrate de que el usuario esté autenticado
    if request.user.is_authenticated:
        # Verifica si el usuario tiene una cuenta asociada
        if hasattr(request.user, 'cuenta') and hasattr(request.user.cuenta, 'cliente'):
            # Filtra las recetas para el cliente asociado a la cuenta del usuario
            recetas_usuario = Receta.objects.filter(cliente=request.user.cuenta.cliente)
            return render(request, 'mis_pedidos.html', {'recetas_usuario': recetas_usuario})
    
    # Manejo para usuarios no autenticados o sin cuenta/cliente asociado
    return render(request, 'mis_pedidos.html', {'recetas_usuario': None})
