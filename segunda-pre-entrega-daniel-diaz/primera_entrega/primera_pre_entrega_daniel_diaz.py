# Modulo para invocar funciones del SO, en este caso para aplicar CLS/Clear (originalmente hice el codigo en visualstudiocode y tengo un toc jeje)
import os
# Modulo datetime para fecha y hora en archivo externo y muestra de datos cargados
import datetime
# Biblioteca de expresiones regulares para validacion de caracteres de usuario valido
import re

# Diccionario vacio
database = {}

# Función de CLS (limpieza de pantalla)
def clear_screen():
  os.system("clear" if os.name == "posix" else "cls")

# Función de ingreso de users
def user_data():
    clear_screen()
    username = input("Ingrese su nombre de usuario (solo letras, números, _ y -): ")

    # Verificar que el nombre de usuario solo contenga letras, números, _ y -
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        print("El nombre de usuario contiene caracteres inválidos. Inténtelo nuevamente.")
        input("Presione una tecla para volver al menu...")
        clear_screen()
        return
    # Se comprueba si el usuario ya existe.
    if username in database:
        print("El nombre de usuario ya existe en la base de datos.")
        input("Presione una tecla para volver al menú...")
        clear_screen()
        return

    password = input("Ingrese su Password (entre 4 y 8 caracteres): ")

    # Verificar que la contraseña tenga una longitud entre 4 y 8 caracteres
    if not 4 <= len(password) <= 8:
        print("La contraseña debe tener entre 4 y 8 caracteres. Inténtelo nuevamente.")
        input("Presione una tecla para volver al menu...")
        clear_screen()
        return

    # Almacenar el usuario y password en el diccionario
    database[username] = password
    print("Usuario ingresado exitosamente!")
    input("Presione una tecla para volver al menú...")

# Función de display de datos
def display_data():
    clear_screen()
    # Se verifica si no hay usuarios registrados
    if not database:
        print("No hay usuarios registrados.")
    else:
        print("Los datos de los usuarios son:\n")
        fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i, (username, password) in enumerate(database.items(), 1):
            print(f"{i}. Usuario: {username} - Password: {password} - Fecha y Hora: {fecha_hora_actual}")

    print("")
    input("Presione una tecla para volver al menú...")

# Función de Login de usuario registrado
def login():
    clear_screen()
    while True:
        user_input = input("Ingrese su nombre de usuario: ")
        #  verifica si existe el usuario
        if user_input not in database:
            input("El usuario no existe. Presione una tecla para intentarlo nuevamente...")
            clear_screen()
            continue
        # Se verifica el ingreso correcto/incorrecto del password
        pass_input = input("Ingrese su Password: ")
        if pass_input == database[user_input]:
            print("Login Exitoso!")
            input("Presione una tecla para volver al menú...")
            break
        else:
            input("Password incorrecto. Presione una tecla para intentarlo nuevamente...")
            clear_screen()

# Función de exportar datos a archivo externo.log; se realiza append al archivo, por lo que se almacenan los datos cargados entre sesiones
def guardar_datos_usuario():
    clear_screen()
    # Se verifica y documenta en el archivo externo si no hay users registrados
    if not database:
        with open("/content/datos_usuarios.log", "a") as archivo:
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"Base de datos de usuarios registrados - Fecha y Hora: {fecha_hora_actual}\n")
            archivo.write("--------------------------------------------------------------------\n")
            archivo.write("No hay usuarios registrados.\n")
            archivo.write(f"Fin de la sesion, Fecha y Hora: {fecha_hora_actual}\n")
            archivo.write("--------------------------------------------------------------------\n")

        print("No hay usuarios registrados. Archivo de registro creado.")
        input("Presione una tecla para volver al menú...")
        return
    # Caso feliz, en donde hay usuarios cargados y se registra fecha y hora en la que cargaron, y se especifica el fin de cada sesion de ejecucion
    try:
        with open("primera_entrega/datos_usuarios.log", "a") as archivo:
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"Base de datos de usuarios registrados - Fecha y Hora: {fecha_hora_actual}\n")
            archivo.write("--------------------------------------------------------------------\n")

            for usuario, password in database.items():
                archivo.write(f"Usuario: {usuario} - Password: {password} - Fecha y Hora: {fecha_hora_actual}\n")

            archivo.write(f"Fin de la sesion, Fecha y Hora: {fecha_hora_actual}\n")
            archivo.write("--------------------------------------------------------------------\n")

        print("Datos guardados exitosamente en 'datos_usuarios.log'.")
        input("Presione una tecla para volver al menú...")
        # Caso no feliz, si por alguna razon no se puede generar o guardar el archivo se mostrará este error.
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        input("Presione una tecla para volver al menú...")


# Funcion de despliegue de menu
def mostrar_menu():
    clear_screen()
    print("\n--- Pre-entrega 1 CoderHouse Python --- \n")
    print("1. Ingresar usuarios")
    print("2. Mostrar datos de usuarios")
    print("3. Iniciar sesión")
    print("4. Guardar datos en archivo")
    print("5. Salir")

# Este bloque de código se ejecutará solo si este script se ejecuta directamente,
# no se ejecutará si se importa como un módulo en otro script.
if __name__ == "__main__":
  # Llamada a la funcion de despliegue de menú
    while True:
        mostrar_menu()
        print("")
        opcion = input("Seleccione una opción: ")
  # Condicionales de cada opcion, los cuales llevan a elegir solo entre las opciones aqui señaladas
        if opcion == "1":
  # Llamada a la funcion de ingreso de usuarios
            user_data()
        elif opcion == "2":
  # Llamada a la funcion de display de los users cargados
            display_data()
        elif opcion == "3":
  # Llamada a la funcion de login
            login()
        elif opcion == "4":
  # Llamada a la funcion de exportar datos de usuarioç
            guardar_datos_usuario()
        elif opcion == "5":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione una tecla para volver al menú...")
