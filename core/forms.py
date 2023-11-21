from django import forms
from .models import Pedido
from .models import Producto


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Selecciona un producto'})


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'