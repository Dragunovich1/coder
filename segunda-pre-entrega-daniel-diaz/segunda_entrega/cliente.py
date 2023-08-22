# Archivo: cliente.py

class Cliente:
    def __init__(self, nombre, apellido, email, saldo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.saldo = saldo
        self.edad = edad

    def realizar_compra(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return f"Compra exitosa. Saldo restante: {self.saldo}"
        else:
            return "Saldo insuficiente para realizar la compra"

    def recargar_saldo(self, monto):
        self.saldo += monto
        return f"Saldo recargado. Saldo actual: {self.saldo}"

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido:  {self.apellido}\nEmail: {self.email}\nSaldo: {self.saldo}\nEdad: {self.edad}"

# Clase derivada (subclase) utilizando herencia
class ClientePremium(Cliente):
    def __init__(self, nombre, apellido, email, saldo, edad, descuento):
        super().__init__(nombre, apellido, email, saldo, edad)
        self.descuento = descuento

    def aplicar_descuento(self, monto):
        monto_con_descuento = monto * (1 - self.descuento / 100)
        return f"Descuento aplicado. Monto con descuento: {monto_con_descuento}"
