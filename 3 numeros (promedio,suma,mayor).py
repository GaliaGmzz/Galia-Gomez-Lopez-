a=int(input("Ingresa un numero entero: "))
b=int(input("Ingresa un numero entero: "))
c=int(input("Ingresa un numero entero: "))
Suma=a+b+c
Prom=Suma/2
if a>b:
    if a>c:
        Max=a
    else:
        Max=c
else:
    if b>c:
        Max=b
    else:
        Max=c
print("El promedio es:",Prom)
print("El suma es:",Suma)
print("El mayor es:",Max)
