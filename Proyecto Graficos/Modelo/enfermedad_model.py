import pandas as pd
import numpy as np


class EnfermedadModel:

    def __init__(self):
        
        self.df = pd.read_csv("diabetes.csv")

    # ======================================
    # TOTAL PACIENTES
    # ======================================
    def total_pacientes(self):
        return len(self.df)

    # ======================================
    # PROMEDIO GLUCOSA
    # ======================================
    def promedio_glucosa(self):
        return np.mean(self.df["Glucose"])

    # ======================================
    # PROMEDIO BMI
    # ======================================
    def promedio_bmi(self):
        return np.mean(self.df["BMI"])

    # ======================================
    # PACIENTES CON DIABETES
    # ======================================
    def pacientes_diabetes(self):
        return len(self.df[self.df["Outcome"] == 1])

    # ======================================
    # PACIENTES SIN DIABETES
    # ======================================
    def pacientes_sanos(self):
        return len(self.df[self.df["Outcome"] == 0])

    # ======================================
    # PACIENTES DE RIESGO
    # ======================================
    def pacientes_riesgo(self):
        return self.df[
            (self.df["Glucose"] > 150) &
            (self.df["BMI"] > 35)
        ].head(20)

    # ======================================
    # PACIENTES MAYORES
    # ======================================
    def pacientes_mayores(self):
        return self.df[self.df["Age"] > 50].head(20)

    # ======================================
    # EJERCICIO ADICIONAL: datos para barras
    # ======================================
    def datos_por_edad(self):
        """Agrupa pacientes en rangos de edad para gráfica de barras."""
        bins = [0, 30, 40, 50, 60, 100]
        labels = ["<30", "30-39", "40-49", "50-59", "60+"]
        self.df["RangoEdad"] = pd.cut(
            self.df["Age"], bins=bins, labels=labels, right=False
        )
        return self.df.groupby("RangoEdad", observed=True)["Outcome"].sum()
