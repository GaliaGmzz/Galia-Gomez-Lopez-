from Modelos.usuario import Usuario

class Bibliotecario(Usuario):

    def __init__(self, nombre, identificacion, area):
        super().__init__(nombre, identificacion, "Bibliotecario")
        self._area = area

    def obtener_area(self):
        return self._area

    def registrar_libro(self, biblioteca, libro):
        biblioteca.agregar_libro(libro)
        print(f"{self.getNombre()} registró el libro '{libro.getTitulo()}'")

    def descripcion(self):
        return f"Bibliotecario del área: {self._area}"

    