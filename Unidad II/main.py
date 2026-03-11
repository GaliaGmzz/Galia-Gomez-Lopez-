from Modelos.libro import Libro
from Modelos.usuario import Usuario
from Servicios.gestorprestamos import GestorPrestamos

libro1= Libro("Pepa pig","Bucanero","12345")
usuario1= Usuario("Valeria","2321578")

gestor= GestorPrestamos()

mensaje= gestor.realizar_prestamo(libro1,usuario1,"2026-03-07")
print(mensaje)
print(libro1.disponibilidad)
gestor.listar_prestamos()

