class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros =[]

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro.getTitulo())
    