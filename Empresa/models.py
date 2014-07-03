from django.db import models
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=128)
    telefone = models.CharField(max_length=12)
    fax = models.CharField(max_length = 12)
    bairro = models.CharField(max_length=32)
    estados = models.CharField(max_length=2, choices=STATE_CHOICES)
    endereco = models.CharField(max_length=256)
    
    
    