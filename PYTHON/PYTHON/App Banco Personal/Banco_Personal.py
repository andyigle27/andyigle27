class AppBancoPersonal:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.usuarios = []

    def menu_principal(self):
        print('---------------------------------')
        print('       [ BANCO PERSONAL ]        ')
        print('---------------------------------')
        print(f'Saldo total: ${self.saldo}')
        print('---------------------------------')
        print('1) 💰 Cuenta Personal')
        print('2) 👥 Préstamos')
        print('3) 📈 Cuenta Luis')
        print('4) 💼 Sueldo')
        print('5) 🔄 Movimientos Terceros')
        print('6) ❌ Salir')
        print('---------------------------------')
        choice = input('--> ')
        while choice not in ['1', '2', '3', '4', '5', '6']:
         print("Opción no válida. Intente de nuevo.")
         choice = input('--> ')
        match choice:
         case '1':
             self.cuenta_personal()
         case '2':
             pass  # Aquí iría la lógica de préstamos
         case '3':
             pass  # Aquí iría la lógica de cuenta Luis
         case '4':
             pass  # Aquí iría la lógica de sueldo
         case '5':
             pass  # Aquí iría la lógica de movimientos terceros
         case '6':
             print("Gracias por usar el Banco Personal. ¡Hasta luego!")
             pass

    def cuenta_personal(self):
        print('---------------------------------')
        print('       [ CUENTA PERSONAL ]      ')
        print('---------------------------------')
        print(f'Saldo bancario: ${self.saldo}')
        print('---------------------------------')
        print('1) Depositar')
        print('2) Retirar')
        print('3) Volver al menú principal')
        sub_choice = input('--> ')
        if sub_choice == '1':
            self.depositar()
        elif sub_choice == '2':
            self.retirar()
        elif sub_choice == '3':
            self.menu_principal()
        else:
            print("Opción no válida. Intente de nuevo.")
            self.cuenta_personal()
            pass

    def depositar(self):
        print('---------------------------------')
        print('       [ DEPOSITAR ]            ')
        print('---------------------------------')
        print('Ingrese el monto a depositar: ')
        monto = float(input('--> '))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            self.depositar()
        else:
            self.saldo += monto
            print(f'Se han depositado ${monto} en su cuenta.')
            self.cuenta_personal()
            pass

    def retirar(self):
        print('---------------------------------')
        print('       [ RETIRAR ]              ')
        print('---------------------------------')
        print('Ingrese el monto a retirar: ')
        monto = float(input('--> '))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            self.retirar()
        elif monto > self.saldo:
            print("Fondos insuficientes.")
            self.retirar()
        else:
            self.saldo -= monto
            print(f'Se han retirado ${monto} de su cuenta.')
            self.cuenta_personal()
            pass

luis_app = AppBancoPersonal("Banco Personal", 5000000)
luis_app.menu_principal()

def maxProfit(self, prices):
    buy = min(prices)
    daybuy = prices.index(buy)
    if daybuy == len(prices):
        profit = 0
    else:
        sell = prices[buy]
        for i in range(daybuy, len(prices)):
            if prices[i] > sell
           sell = prices[i]
        profit = sell - buy
        return profit