from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CrearCuentaForm
from .forms import IniciarSesionForm


def registro(request):
    if request.method == 'POST':
        form = CrearCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a una página de éxito o realiza alguna acción apropiada
            return redirect('pagina_principal')
    else:
        form = CrearCuentaForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    error_message = None

    if request.method == 'POST':
        form = IniciarSesionForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirige al usuario a una página de éxito o realiza alguna acción apropiada
                return redirect('pagina_principal')
            
            
    else:
        form = IniciarSesionForm()

    return render(request, 'inicio_sesion.html', {'form': form, 'error_message': error_message})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')  # Redirige al usuario al inicio de sesión después del cierre de sesión


def home(request):
    # Lógica para la página de inicio
    return render(request, 'home.html')
