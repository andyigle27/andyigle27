class Usuario:
    def __init__(self, nombre, balance=0):
        self.nombre = nombre
        self.balance = balance
        self.prestamos = [] 

    def depositar(self, monto):
        self.balance += monto
        print(f"💰 Depósito de {monto}. Nuevo balance: {self.balance}")

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f"💸 Retiro de {monto}. Nuevo balance: {self.balance}")
        else:
            print("❌ Fondos insuficientes")

    def ver_balance(self):
        print(f"👤 Usuario: {self.nombre}, Balance: {self.balance}")

class Prestamo:
    def __init__(self, monto, interes, plazo):
        self.monto = monto
        self.interes = interes
        self.plazo = plazo
        self.pagado = False 

    def calcular_cuota_mensual(self):
        cuota = (self.monto * (1 + self.interes/100)) / self.plazo
        return round(cuota, 2)

    def pagar_cuota(self, monto):
        self.pagado += monto
        print(f"✅ Pago realizado: {monto}, Total pagado: {self.pagado}")
    
    def estado_prestamo(self):
        if self.pagado == True:
            print("✅ Préstamo pagado en su totalidad.")
        else:
            print("❌ Préstamo pendiente de pago.")

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"👥 Usuario {usuario.nombre} agregado al banco {self.nombre}")

    def otorgar_prestamo(self, usuario, monto, interes, plazo):
        prestamo = Prestamo(monto, interes, plazo)
        usuario.prestamos.append(prestamo)
        usuario.depositar(monto)  # el préstamo entra a su balance
        print(f"🏦 Prestamo de {monto} otorgado a {usuario.nombre}")
    
    def ver_usuarios(self):
        for usuario in self.usuarios:
            usuario.ver_balance()


