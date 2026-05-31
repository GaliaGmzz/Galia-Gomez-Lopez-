import pandas as pd

class DiabetesModel:
    def __init__(self):
        self.df = pd.read_csv("C:/Users/gomez/OneDrive/Documentos/Programación/Programacion 2/Proyecto Diabetes/diabetes.csv")

    def total_pacientes(self):
        return len(self.df)

    def promedio_glucosa(self):
        return round(self.df["Glucose"].mean(), 2)

    def pacientes_diabetes(self):
        return len(self.df[self.df["Outcome"] == 1])

    def promedio_embarazos_diabetes(self):
        diabetes = self.df[self.df["Outcome"] == 1]
        return round(diabetes["Pregnancies"].mean(), 2)

    def promedio_edad(self):
        return round(self.df["Age"].mean(), 2)

    def pacientes_riesgo(self):
        riesgo = self.df[
            (self.df["Glucose"] > 180) & (self.df["BMI"] > 40)
        ]
        return riesgo.head(20)  

