from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.triangulo import Triangulo

def menu():

    while True:
        
        print("\n--- MENÚ FIGURA A ELEGIR ---")
        print("1. Circulo")
        print("2. Cuadrado")
        print("3. Triangulo")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            radio = float(input("Dame el radio del circulo: "))
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.area()}")
            print(f"El perímetro del círculo es: {circulo.perimetro()}")
        
        elif opcion == "2":
            lado = float(input("Dame el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.area()}")
            print(f"El perímetro del cuadrado es: {cuadrado.perimetro()}")
        
        elif opcion == "3":
            base = float(input("Dame la base del triangulo: "))
            altura = float(input("Dame la altura del triangulo: "))
            lado1 = float(input("Dame el lado 1 del triangulo: "))
            lado2 = float(input("Dame el lado 2 del triangulo: "))
            lado3 = float(input("Dame el lado 3 del triangulo: "))
            triangulo = Triangulo(base, altura, lado1, lado2, lado3)
            print(f"El área del triangulo es: {triangulo.area()}")
            print(f"El perímetro del triangulo es: {triangulo.perimetro()}")

        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("\n[ERROR] Opción inválida. Debes elegir entre 1 y 4.")
            continue

        
if __name__ == "__main__":
    menu()




