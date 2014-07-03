from django.contrib import admin
from pedido.models import Pedido
from pedido.models import Produto




class ProdutoInline(admin.StackedInline):
    model = Pedido.produtos.through
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero','status')
    inlines = (ProdutoInline,)

# Register your models here.
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Produto)