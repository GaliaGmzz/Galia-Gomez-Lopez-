# O(1) — Tiempo Constante
def obtener_ultimo_elemento(lista):
    return lista[-1]

numeros = [10, 20, 30, 40, 50]
print(obtener_ultimo_elemento(numeros))

# O(log n) — Logarítmico
def dividir_entre_tres(n):
    contador = 0
    while n > 1:
        n = n // 3
        contador += 1
    return contador
print(dividir_entre_tres(243))

# O(n) — Lineal
def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

print(contar_pares([1,2,3,4,5,6]))

# O(n log n)
def mezcla_lineal_log(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2

# O(n²) — Cuadrática
def comparar_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])

comparar_lista([1,2,3])

# O(2ⁿ) — Exponencial
def generar_binarios(n):
    if n == 0:
        return 1
    return generar_binarios(n-1) + generar_binarios(n-1)

print(generar_binarios(5))

# O(n!) — Factorial
def permutar(lista, inicio=0):
    if inicio == len(lista):
        print(lista)
        return

    for i in range(inicio, len(lista)):
        lista[inicio], lista[i] = lista[i], lista[inicio]
        permutar(lista, inicio + 1)
        lista[inicio], lista[i] = lista[i], lista[inicio]


permutar([1, 2, 3])
