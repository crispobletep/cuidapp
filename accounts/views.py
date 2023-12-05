from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CrearCuentaForm
from .models import Cuenta
from core.models import Cliente


def registro(request):
    if request.method == 'POST':
        form = CrearCuentaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            rol = form.cleaned_data['rol']
            rut = form.cleaned_data['rut']

            try:
                user = Cuenta.objects.create_user(username=username, password=password, rol=rol)
                if rol == 'usuario':
                    # Crea la instancia de Cliente y asocia al usuario
                    cliente = Cliente.objects.create(nombre=username, rut=rut, cuenta=user)

                login(request, user)
                messages.success(request, '¡Registro exitoso! Ahora estás conectado.')

                return redirect('pagina_principal')

            except Exception as e:
                messages.error(request, f'Error en el registro: {str(e)}')
        else:
            messages.error(request, 'Error en el formulario de registro. Por favor, corrige los errores.')
    else:
        form = CrearCuentaForm()

    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    error_message = None
    if request.user.is_authenticated:
        return redirect('/inicio')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print(f"Usuario autenticado: {user.username}")
                return redirect('/inicio')
            else:
                print("Nombre de usuario o contraseña incorrectos.")
                error_message = "Nombre de usuario o contraseña incorrectos."
    else:
        form = AuthenticationForm()

    return render(request, 'inicio_sesion.html', {'form': form, 'error_message': error_message})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')  # Redirige al usuario al inicio de sesión después del cierre de sesión


def home(request):
    # Lógica para la página de inicio
    return render(request, 'home.html')
