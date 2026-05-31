import flet as ft
from modelo.diabetes_model import DiabetesModel

class DiabetesController:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = DiabetesModel()

    def mostrar_estadisticas(self, e):
        total = self.modelo.total_pacientes()
        glucosa = self.modelo.promedio_glucosa()
        diabetes = self.modelo.pacientes_diabetes()
        embarazos = self.modelo.promedio_embarazos_diabetes()
        edad = self.modelo.promedio_edad()  # NUEVA ESTADÍSTICA

        self.vista.resultado.value = f"""
        Total pacientes: {total}
        Promedio glucosa: {glucosa}
        Pacientes con diabetes: {diabetes}
        Promedio embarazos con diabetes: {embarazos}
        Promedio edad: {edad}
        """
        self.vista.page.update()

    def mostrar_riesgo(self, e):
        self.vista.limpiar_tabla()
        riesgo = self.modelo.pacientes_riesgo()

        for _, fila in riesgo.iterrows():
            tarjeta = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Glucosa: {fila['Glucose']}"),
                        ft.Text(f"BMI: {fila['BMI']}"),
                        ft.Text(f"Edad: {fila['Age']}")
                    ]
                ),
                padding=10,
                border=ft.border.all(1, "gray"),
                border_radius=10,
                bgcolor="lightyellow"  
            )
            self.vista.tabla.controls.append(tarjeta)

        self.vista.page.update()
