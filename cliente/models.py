from django.db import models
from django.core.validators import RegexValidator
from django.forms import ModelForm

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(validators=[RegexValidator(r'(^\d{3}\.\d{3}\.\d{3}-\d{2})|(^\d{3}\d{3}\d{3}\d{2})$')])
    telefone = models.CharField(validators=[RegexValidator(r'(^\d{3]\-d{4}\-\d{4}')])
    
    
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'rg']
        