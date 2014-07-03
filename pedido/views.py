from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from pedido.models import Pedido 
from pedido.forms import PedidoForm
from django.template import RequestContext

def index(request):
   
    
    PedidoFormSet = modelformset_factory(Pedido, form=PedidoForm)
    if request.method == 'POST':
        formset = PedidoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
           
    else:
        formset = PedidoFormSet()
        
    csrfContext = RequestContext(request,{"formset": formset})

    return render_to_response("pedido/index.html", csrfContext)