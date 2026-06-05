import flet as ft
import matplotlib.pyplot as plt

from Modelo.enfermedad_model import EnfermedadModel


class EnfermedadController:

    def __init__(self, vista):
        self.vista = vista
        self.modelo = EnfermedadModel()

    # ======================================
    # ESTADÍSTICAS
    # ======================================
    def mostrar_estadisticas(self, e):
        total = self.modelo.total_pacientes()
        glucosa = self.modelo.promedio_glucosa()
        bmi = self.modelo.promedio_bmi()
        diabetes = self.modelo.pacientes_diabetes()
        sanos = self.modelo.pacientes_sanos()

        self.vista.resultado.value = (
            f"Total pacientes: {total}\n"
            f"Promedio glucosa: {glucosa:.2f}\n"
            f"Promedio BMI: {bmi:.2f}\n"
            f"Pacientes con diabetes: {diabetes}\n"
            f"Pacientes sanos: {sanos}"
        )

        self.vista.page.update()

        # ======================================
        # GRÁFICA DE PASTEL
        # ======================================
        datos = [diabetes, sanos]
        etiquetas = ["Diabetes", "Sanos"]

        plt.figure(figsize=(6, 6))
        plt.pie(datos, labels=etiquetas, autopct="%1.1f%%", startangle=140)
        plt.title("Pacientes con y sin diabetes")
        plt.tight_layout()
        plt.show()

    # ======================================
    # TABLA PACIENTES RIESGO
    # ======================================
    def mostrar_riesgo(self, e):
        self.vista.tabla.rows.clear()
        datos = self.modelo.pacientes_riesgo()

        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(fila["Glucose"]))),
                        ft.DataCell(ft.Text(str(fila["BMI"]))),
                        ft.DataCell(ft.Text(str(fila["Age"]))),
                        ft.DataCell(ft.Text(str(fila["Outcome"]))),
                    ]
                )
            )

        self.vista.page.update()

    # ======================================
    # TABLA PACIENTES MAYORES
    # ======================================
    def mostrar_mayores(self, e):
        self.vista.tabla.rows.clear()
        datos = self.modelo.pacientes_mayores()

        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(fila["Glucose"]))),
                        ft.DataCell(ft.Text(str(fila["BMI"]))),
                        ft.DataCell(ft.Text(str(fila["Age"]))),
                        ft.DataCell(ft.Text(str(fila["Outcome"]))),
                    ]
                )
            )

        self.vista.page.update()

    # ======================================
    # EJERCICIO ADICIONAL: GRÁFICA DE BARRAS
    # ======================================
    def mostrar_barras(self, e):
        datos = self.modelo.datos_por_edad()

        plt.figure(figsize=(8, 5))
        plt.bar(datos.index, datos.values, color="steelblue", edgecolor="black")
        plt.title("Pacientes con diabetes por rango de edad")
        plt.xlabel("Rango de edad")
        plt.ylabel("Cantidad con diabetes")
        plt.tight_layout()
        plt.show()
