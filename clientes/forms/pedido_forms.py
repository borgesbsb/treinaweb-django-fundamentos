from django import forms
from ..models import Pedido

class PedidoForm(forms.ModelForm):
    pedido = forms.ModelChoiceField(queryset=Pedido.objects.all())
    class Meta:
        model = Pedido
        fields = ['cliente','data_pedido', 'valor', 'status', 'observacoes' ]
    