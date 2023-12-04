from django import forms
from .models import Producto, Medicamento


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['medicamento', 'precio', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicamento'].queryset = Medicamento.objects.all()
        self.fields['medicamento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre del medicamento'})
        self.fields['precio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Precio del producto'})
        self.fields['imagen'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagen del producto'})
