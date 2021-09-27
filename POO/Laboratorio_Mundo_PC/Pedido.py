class Pedido:
    contadorOrden = 0
    def __init__(self, computadora):
        Pedido.contadorOrden += 1
        self._idPedido = Pedido.contadorOrden
        self._computadora = computadora

    def agregarPedido(self, pedido):
        self._computadora.append(pedido)

    def __str__(self):
        pedidos_str = ''
        for pedido in self._computadora:
            pedidos_str += pedido.__str__()

        return f'''
        ID Pedido: {self._idPedido} \n
        Descripcion {pedidos_str}
        '''