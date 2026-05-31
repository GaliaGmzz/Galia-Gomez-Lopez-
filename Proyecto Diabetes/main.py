import pandas as pd

#leer archivo
df = pd.read_csv(r"C:\Users\gomez\OneDrive\Documentos\Programación\Programacion 2\Proyecto Diabetes\Diabetes\diabetes.csv")

#Filtrar todos los pacientes que tienen diabetes
diabetes = df[df["Outcome"] == 1]

print("Personas con diabetes")
print(diabetes)

promedio = diabetes["Pregnancies"].mean()

print("Promedio de embarazos: ")
print (promedio)

personas_riesgo = df[(df["Glucose"]> 150) & (df["BMI"] > 35) & (df["Age"]> 50)]
print(personas_riesgo)

#Porcentaje de personas con diabetes

#Porcentaje = personas con diabetes/total * 100

total = len (df)
personas_con_diabetes = len(diabetes)

porcentaje = personas_con_diabetes/total*100
print(f"Porcentaje: {porcentaje}%")

#max()
personas_con_glucosa = df["Glucose"].max()
print(personas_con_glucosa)

promedios_glucosa_por_diagnosticos = df.groupby("Outcome")["Glucose"].mean()
print (promedios_glucosa_por_diagnosticos)

promedio_presion_arterial_todo = df.mean()
promedio_presion_arterial = df[df["BloodPressure"] > 60].mean()

print (f" Presion arterial todos = {promedio_presion_arterial_todo}")
print (f" Presion arterial correcta = {promedio_presion_arterial}")

#Ordenamiento

ordenados = df.sort_values(
    by = "Glucose",
    ascending=False
)

print(ordenados)