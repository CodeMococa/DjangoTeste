from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from Empresa.models import Empresa
from Empresa.forms import EmpresaForm
from django.template import RequestContext

def index(request):
   
    
    EmpresaFormSet = modelformset_factory(Empresa, form=EmpresaForm)
    if request.method == 'POST':
        formset = EmpresaFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
           
    else:
        formset = EmpresaFormSet()
        
    csrfContext = RequestContext(request,{"formset": formset})

    return render_to_response("Empresa/index.html", csrfContext)