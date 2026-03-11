from Modelos.prestamo import Prestamo

class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    def realizar_prestamo(self,libro,usuario,fecha):
        if libro.prestar():
            prestamo = Prestamo(libro,fecha,usuario)
            self.prestamos.append(prestamo)
            return "Prestamo realizado correctamente"
        return "El libro no esta disponible"

    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)
