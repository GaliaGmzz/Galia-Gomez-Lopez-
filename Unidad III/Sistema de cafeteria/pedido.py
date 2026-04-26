class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = sum([p.get_precio() for p in self._productos])
        # Aplicar descuento si es ClienteFrecuente
        if hasattr(self._cliente, "obtener_descuento"):
            total *= (1 - self._cliente.obtener_descuento())
        return total

    def __str__(self):
        productos_str = "\n".join([str(p) for p in self._productos])
        return f"Pedido de {self._cliente._nombre}:\n{productos_str}\nTotal: ${self.calcular_total()}"

        