import flet as ft
from vista.diabetes_view import DiabetesView
from controller.diabetes_controller import DiabetesController

def main(page: ft.Page):
    vista = DiabetesView(page)

    controlador = DiabetesController(vista)

    vista.btn_estadisticas.on_click = controlador.mostrar_estadisticas
    vista.btn_riesgo.on_click = controlador.mostrar_riesgo

    page.add(vista.construir())

ft.app(target=main)
