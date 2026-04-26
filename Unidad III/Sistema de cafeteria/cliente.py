class Cliente:
    def __init__(self, nombre, identificador):
        self._nombre = nombre
        self._identificador = identificador

    def __str__(self):
        return f"Cliente: {self._nombre} (ID: {self._identificador})"

    

