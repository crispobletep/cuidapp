from django import forms
from .models import Cuenta
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
        fields = ['username', 'rol']


