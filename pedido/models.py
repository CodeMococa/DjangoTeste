from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=128)
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data = models.DateField()
    numero = models.CharField(max_length=20)
    status = models.CharField(max_length='1',choices=(
                                                      ('A','Aberto'),
                                                      ('E','Encerrado'),
                                                      ('C','Cancelado'),
                                                      ('P','Pendente'),
                                                      ('N','Nao Aprovado'),
                                                      ))
    produtos = models.ManyToManyField(Produto, through='ItensDoPedido')
    
    def __str__(self):
        return 'Pedido ' + self.numero
    
class ItensDoPedido(models.Model):
    pedido = models.ForeignKey(Pedido)
    produto = models.ForeignKey(Produto)
    quantidade = models.DecimalField(max_digits=6,decimal_places=4)
    valor_unitario = models.DecimalField(max_digits=8,decimal_places=2)
    
    