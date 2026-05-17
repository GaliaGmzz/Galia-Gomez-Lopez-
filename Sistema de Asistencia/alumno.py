class Alumno: 
    def __init__(self, nombre, presente, grupo, materia):
        self.nombre = nombre
        self.presente = presente
        self.grupo = grupo 
        self.materia = materia
    
    def __str__(self):
        estado = "Presente" if self.presente else "Ausente"
        return f"{self.nombre} - {estado} - Grupo: {self.grupo or 'N/A'} - Materia: {self.materia or 'N/A'}"

    def limpiar(self):
        self.grupo = None
        self.materia = None

    def validar(self):
        if not self.nombre or self.presente is None or not self.grupo or not self.materia:
            return "Error: faltan datos"
        return "Datos completos"