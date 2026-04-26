from cliente import Cliente

class ClienteFrecuente(Cliente):
    def __init__(self, nombre, identificador, descuento=0.1):
        super().__init__(nombre, identificador)
        self._descuento = descuento

    def obtener_descuento(self):
        return self._descuento

    def __str__(self):
        return f"Cliente Frecuente: {self._nombre} (ID: {self._identificador}, Descuento: {self._descuento*100}%)"

