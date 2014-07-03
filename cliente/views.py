from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from cliente.models import Cliente

# Create your views here.

def exibeCliente(request):
    ClienteFormSet = modelformset_factory(Cliente)
    if request.method == 'POST':
        formset = ClienteFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
        else:
            formSet = ClienteFormSet()
        return render_to_response("gerencia.html",{"formset",formset,})
