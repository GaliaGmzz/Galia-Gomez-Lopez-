from Modelos.libro import Libro
from Modelos.biblioteca import Biblioteca
from Modelos.bibliotecario import Bibliotecario
from Modelos.alumno import Alumno
from Servicios.gestorprestamos import GestorPrestamos
from Modelos.usuario import Usuario

#Crear biblioteca
biblioteca = Biblioteca ("Biblioteca Central")

#Crear bibliotecario
bibliotecario1 = Bibliotecario ("Carlos", "B001", "IA") 

#Crear libros
libro1 = Libro("Pepa Pig", "Bucanero", "12345")
libro2 = Libro("Teoría de Evolución del Ser Humano", "Jorge el curioso", "12345")

#Bibliotecario registra libros
bibliotecario1.registrar_libro(biblioteca, libro1)
bibliotecario1.registrar_libro(biblioteca, libro2)

#Libros disponibles
biblioteca.listar_libros()

#Crear usuario
alumno = Alumno("Galia", "2210431", "Alumno")

#Crear gestor de prestamos
gestor = GestorPrestamos()

#Realizar prestamo
print(gestor.realizar_prestamo(libro1, alumno, "18-04-2026"))

#Imprimir prestamos
gestor.listar_prestamos()

print(bibliotecario1.descripcion())
print(alumno.descripcion())


