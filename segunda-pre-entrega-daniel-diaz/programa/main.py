from cliente import Cliente, ClientePremium

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    saldo = float(input("Ingrese el saldo del cliente: "))
    edad = int(input("Ingrese la edad del cliente: "))
    return Cliente(nombre, email, saldo, edad)

def crear_cliente_premium():
    nombre = input("Ingrese el nombre del cliente premium: ")
    email = input("Ingrese el email del cliente premium: ")
    saldo = float(input("Ingrese el saldo del cliente premium: "))
    edad = int(input("Ingrese la edad del cliente premium: "))
    descuento = float(input("Ingrese el porcentaje de descuento para el cliente premium: "))
    return ClientePremium(nombre, email, saldo, edad, descuento)

def realizar_compra(cliente):
    monto = float(input("Ingrese el monto de la compra: "))
    print(cliente.realizar_compra(monto))

def recargar_saldo(cliente):
    monto = float(input("Ingrese el monto de la recarga de saldo: "))
    print(cliente.recargar_saldo(monto))

def aplicar_descuento(cliente_premium):
    monto = float(input("Ingrese el monto de la compra para el cliente premium: "))
    print(cliente_premium.aplicar_descuento(monto))

def main():
    print("Bienvenido al programa de Clientes en una página de compras\n")

    while True:
        print("1. Crear Cliente")
        print("2. Crear Cliente Premium")
        print("3. Realizar Compra")
        print("4. Recargar Saldo")
        print("5. Aplicar Descuento")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cliente = crear_cliente()
            print("\nCliente creado:")
            print(cliente)
        elif opcion == "2":
            cliente_premium = crear_cliente_premium()
            print("\nCliente premium creado:")
            print(cliente_premium)
        elif opcion == "3":
            realizar_compra(cliente)
        elif opcion == "4":
            recargar_saldo(cliente)
        elif opcion == "5":
            aplicar_descuento(cliente_premium)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()