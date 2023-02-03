from ..models import Pedido


def cadastrar_pedido(pedido):
    pedido_bd = Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido,
                                      valor=pedido.valor, status=pedido.status, observacoes=pedido.observacoes)
    pedido_bd.save()