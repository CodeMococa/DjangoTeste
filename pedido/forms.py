
from form_utils.forms import BetterModelForm
from django.forms import ModelForm
from pedido.models import Pedido,Produto 

class PedidoForm(BetterModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
 
class ProdutoForm(BetterModelForm):
    class Meta:
        model = Produto
        fields = '__all__'     
