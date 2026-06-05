import flet as ft


class EnfermedadView:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Dashboard Enfermedades"
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.scroll = "auto"

        # ======================================
        # BOTONES
        # ======================================
        self.btn_estadisticas = ft.ElevatedButton(
            "Estadísticas",
            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE),
        )

        self.btn_riesgo = ft.ElevatedButton(
            "Pacientes Riesgo",
            style=ft.ButtonStyle(bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE),
        )

        self.btn_mayores = ft.ElevatedButton(
            "Pacientes Mayores",
            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE),
        )

        # EJERCICIO ADICIONAL
        self.btn_barras = ft.ElevatedButton(
            "Gráfica de Barras",
            style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_700, color=ft.Colors.WHITE),
        )

        # ======================================
        # RESULTADOS
        # ======================================
        self.resultado = ft.Text(size=18)

        # TABLA
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Glucosa", weight="bold")),
                ft.DataColumn(ft.Text("BMI", weight="bold")),
                ft.DataColumn(ft.Text("Edad", weight="bold")),
                ft.DataColumn(ft.Text("Resultado", weight="bold")),
            ],
            rows=[],
        )

    # ======================================
    # INTERFAZ
    # ======================================
    def construir(self):
        return ft.Column(
            controls=[
                ft.Text(
                    "Sistema de Visualización de Diabetes",
                    size=32,
                    weight="bold",
                    color=ft.Colors.BLUE_800,
                ),
                ft.Text(
                    "Dataset: Pima Indians Diabetes",
                    size=14,
                    color=ft.Colors.GREY_600,
                ),
                ft.Row(
                    controls=[
                        self.btn_estadisticas,
                        self.btn_riesgo,
                        self.btn_mayores,
                        self.btn_barras,
                    ]
                ),
                ft.Divider(),
                self.resultado,
                self.tabla,
            ],
            spacing=20,
        )
