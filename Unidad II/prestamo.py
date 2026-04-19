class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha_prestamo = fecha_prestamo

    def getLibro(self):
        return self.__libro
    
    def getUsuario(self):
        return self.__usuario
    
    def getFechaPrestamo(self):
        return self.__fecha_prestamo
    
    def __str__(self):
        return f"{self.__usuario} - {self.__libro}"
