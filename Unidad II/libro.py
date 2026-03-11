class Libro:
    def __init__(self,autor,titulo,isbn):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        self.disponibilidad=True
    def prestar (self):
        if (self.disponibilidad):
            self.disponibilidad=False
            return False
    def devolver(self):
        self.disponibilidad=True