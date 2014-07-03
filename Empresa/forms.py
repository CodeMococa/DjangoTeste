from django.forms import ModelForm
from Empresa.models import Empresa
from localflavor.br.forms import BRPhoneNumberField

class EmpresaForm(ModelForm):
    telefone = BRPhoneNumberField(required=True)
    class Meta:
        model = Empresa
        fields = '__all__'
      
