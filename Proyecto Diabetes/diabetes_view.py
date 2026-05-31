import flet as ft

class DiabetesView:
    def __init__(self, page: ft.Page):
        self.page = page

        self.page.title = "Análisis Dataset Diabetes"
        self.page.window_width = 900
        self.page.window_height = 750
        self.page.padding = 20
        self.page.bgcolor = "lightblue"  

        self.btn_estadisticas = ft.ElevatedButton(
            "Mostrar estadísticas", bgcolor="green", color="white"
        )
        self.btn_riesgo = ft.ElevatedButton(
            "Pacientes de riesgo", bgcolor="red", color="white"
        )

        self.resultado = ft.Text(size=18)
        self.tabla = ft.Column()

    def construir(self):
        return ft.Column(
            controls=[
                ft.Text("Sistema de Análisis Diabetes", size=30, weight="bold"),
                ft.Divider(),
                ft.Row(controls=[self.btn_estadisticas, self.btn_riesgo]),
                ft.Divider(),
                self.resultado,
                self.tabla
            ],
            spacing=20
        )

    def limpiar_tabla(self):
        self.tabla.controls.clear()
