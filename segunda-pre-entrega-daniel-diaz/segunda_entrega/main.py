import os
import re
from cliente import Cliente, ClientePremium

# Función de CLS (limpieza de pantalla)
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Función para ingresar un valor numérico con validación
def input_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error en la entrada. Intente nuevamente.")

# Función para ingresar un valor entero con validación dentro de un rango
def input_entero_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"El valor debe estar entre {minimo} y {maximo}. Intente nuevamente.")
        except ValueError:
            print("Error en la entrada. Intente nuevamente.")

# Función para ingresar una dirección de correo electrónico válida
def input_email(mensaje):
    while True:
        valor = input(mensaje)
        if re.match(r"[^@]+@[^@]+\.[^@]+", valor):
            return valor
        else:
            print("Correo electrónico inválido. Intente nuevamente.")

# Función para ingresar un nombre válido (solo letras)
def input_nombre(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isalpha():
            return valor
        else:
            print("Nombre inválido. Intente nuevamente.")

# Función para ingresar un apellido válido (solo letras)
def input_apellido(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isalpha():
            return valor
        else:
            print("Apellido inválido. Intente nuevamente.")

# Funcion de crear el cliente normal
def crear_cliente():
    nombre = input_nombre("Ingrese el nombre del cliente: ")
    apellido = input_apellido("Ingrese el apellido del cliente: ")
    email = input_email("Ingrese el email del cliente: ")
    saldo = input_numero("Ingrese el saldo del cliente: ")
    edad = input_entero_rango("Ingrese la edad del cliente: ", 1, 120)
    return Cliente(nombre, apellido, email, saldo, edad)

# Funcion de crear el cliente premium
def crear_cliente_premium():
    nombre = input_nombre("Ingrese el nombre del cliente premium: ")
    apellido = input_apellido("Ingrese el apellido del cliente premium: ")
    email = input_email("Ingrese el email del cliente premium: ")
    saldo = input_numero("Ingrese el saldo del cliente premium: ")
    edad = input_entero_rango("Ingrese la edad del cliente premium: ", 1, 120)
    descuento = input_numero("Ingrese el porcentaje de descuento para el cliente premium: ")
    return ClientePremium(nombre, apellido, email, saldo, edad, descuento)

# Funcion de seleccionar cliente, dentro de la lista de clientes creados
def seleccionar_cliente(clientes):
    print("\nClientes disponibles:")
    for index, cliente in enumerate(clientes, start=1):
        print(f"{index}. {cliente.nombre} {cliente.apellido}")
    while True:
        try:
            seleccion = int(input("\nSeleccione un cliente: "))
            if 1 <= seleccion <= len(clientes):
                return clientes[seleccion - 1]
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

# Funcion de realizar la compra, si el cliente es premium se aplica el descuento.
def realizar_compra(cliente):
    while True:
        monto = input_numero("Ingrese el monto de la compra: ")
        if isinstance(cliente, ClientePremium):
            print("El cliente es premium. Se aplicará el descuento.")
            monto_con_descuento = monto * (1 - cliente.descuento / 100)
            print(f"Monto con descuento: {monto_con_descuento}")
            if monto_con_descuento <= cliente.saldo:
                cliente.saldo -= monto_con_descuento
                print(f"Compra exitosa. Saldo restante: {cliente.saldo}")
            else:
                print("Saldo insuficiente para realizar la compra.")
        else:
            if monto <= cliente.saldo:
                cliente.saldo -= monto
                print(f"Compra exitosa. Saldo restante: {cliente.saldo}")
            else:
                print("Saldo insuficiente para realizar la compra.")
        break

# Funcion de recargar saldo, se creo para realizar pruebas sin tener que crear clientes extra
def recargar_saldo(cliente):
    while True:
        monto = input_numero("Ingrese el monto de la recarga de saldo: ")
        cliente.saldo += monto
        print(f"Saldo recargado. Saldo actual: {cliente.saldo}")
        break

# Menu
def main():
    clientes = []  # Lista para almacenar los clientes creados

    while True:
        clear_screen()
        print("\n--- Pre-entrega 2 CoderHouse Python --- \n")
        print("1. Crear Cliente")
        print("2. Crear Cliente Premium")
        print("3. Realizar Compra")
        print("4. Recargar Saldo")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cliente = crear_cliente()
            clientes.append(cliente)  # Agregar el cliente a la lista
            print("\nCliente creado:")
            print(cliente)
            input("\nPresione una tecla para continuar...")
        elif opcion == "2":
            cliente_premium = crear_cliente_premium()
            clientes.append(cliente_premium)  # Agregar el cliente premium a la lista
            print("\nCliente premium creado:")
            print(cliente_premium)
            input("\nPresione una tecla para continuar...")
        elif opcion == "3":
            if clientes:
                cliente = seleccionar_cliente(clientes)
                realizar_compra(cliente)
                input("\nPresione una tecla para continuar...")
            else:
                print("No hay clientes creados. Crea un cliente primero.")
                input("\nPresione una tecla para continuar...")
        elif opcion == "4":
            if clientes:
                cliente = seleccionar_cliente(clientes)
                recargar_saldo(cliente)
                input("\nPresione una tecla para continuar...")
            else:
                print("No hay clientes creados. Crea un cliente primero.")
                input("\nPresione una tecla para continuar...")
        elif opcion == "5":
            print("Hasta luegoo!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            input("\nPresione una tecla para continuar...")

if __name__ == "__main__":
    main()