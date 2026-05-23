import numpy as np

numeros = np.array([1,7,8,3])

resultado = numeros + 5
res = numeros **5

promedio = np.mean(numeros)
maximo = np.max(numeros)
minimo = np.min(numeros)
suma = np.sum(numeros)

print(f"Promedio: {promedio}")
print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")
print(f"Suma: {suma}")
print(resultado)
print(res)

