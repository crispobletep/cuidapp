from django import forms
from .models import Cuenta
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator


class CrearCuentaForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                message="La contraseña debe tener al menos una mayúscula, un número y un carácter especial."
            )
        ]
    )

    class Meta:
        model = Cuenta
        fields = ['usuario', 'password', 'rol']


class IniciarSesionForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                message="La contraseña debe tener al menos una mayúscula, un número y un carácter especial."
            )
        ]
    )





