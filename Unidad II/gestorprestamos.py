from Modelos.prestamo import Prestamo
class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    def realizar_prestamo(self, libro, usuario, fecha):
        if libro.prestar():
            prestamo = Prestamo(libro, usuario, fecha)
            self.prestamos.append(prestamo)
            return "Préstamo realizado correctamente"
        return "El libro no está disponible"
    
    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)
