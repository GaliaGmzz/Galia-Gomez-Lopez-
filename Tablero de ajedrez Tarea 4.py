print("TableroAjedrezPotencias(Algoritmo)\n")
print("Definir fila, columna, n Como Entero")
print("n ← 0")
print("Para fila ← 1 Hasta 8 Hacer")
print("Para columna ← 1 Hasta 8 Hacer")
print("Escribir 2 ^ n Sin Saltar n ← n + 1")
print("FinPara Escribir """)
print("FinPara")
print("FinAlgoritmo")
print("\nTableroAjedrezPotencias(Python)\n")
n = 0
for fila in range(8):
    for columna in range(8):
        print(2**n, end=" ")
        n += 1
    print()
