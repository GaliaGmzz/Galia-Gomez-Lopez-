from cliente import Cliente
from clientefrecuente import ClienteFrecuente
from producto import Producto
from pedido import Pedido
from cafeteria import Cafeteria

def main():
    # Crear cafetería
    cafeteria = Cafeteria("Café Central")

    # Crear clientes
    cliente1 = Cliente("Ana", 1)
    cliente2 = ClienteFrecuente("Luis", 2, descuento=0.15)

    cafeteria.registrar_cliente(cliente1)
    cafeteria.registrar_cliente(cliente2)

    # Crear productos
    producto1 = Producto("Capuchino", 50)
    producto2 = Producto("Croissant", 30)

    cafeteria.registrar_producto(producto1)
    cafeteria.registrar_producto(producto2)

    # Crear pedidos
    pedido1 = Pedido(cliente1)
    pedido1.agregar_producto(producto1)
    pedido1.agregar_producto(producto2)

    pedido2 = Pedido(cliente2)
    pedido2.agregar_producto(producto1)

    cafeteria.crear_pedido(pedido1)
    cafeteria.crear_pedido(pedido2)

    # Mostrar resultados
    print(cafeteria)
    cafeteria.listar_pedidos()

if __name__ == "__main__":
    main()
