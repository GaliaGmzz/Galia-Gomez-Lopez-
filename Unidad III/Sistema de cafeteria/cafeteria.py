class Cafeteria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._clientes = []
        self._productos = []
        self._pedidos = []

    def registrar_cliente(self, cliente):
        self._clientes.append(cliente)

    def registrar_producto(self, producto):
        self._productos.append(producto)

    def crear_pedido(self, pedido):
        self._pedidos.append(pedido)

    def listar_pedidos(self):
        for pedido in self._pedidos:
            print(pedido)

    def __str__(self):
        return f"Cafetería: {self._nombre}"

