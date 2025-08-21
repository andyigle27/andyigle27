
def menu_principal():
    print('---------------------------------')
    print('       [ BANCO PERSONAL ]        ')
    print('---------------------------------')
    print('Saldo total: $')
    print('---------------------------------')
    print('1) 💰 Cuenta Personal')
    print('2) 👥 Préstamos')
    print('3) 📈 Cuenta Luis')
    print('4) 💼 Sueldo')
    print('5) 🔄 Movimientos Terceros')
    print('6) ❌ Salir')
    print('---------------------------------')

class CuentaPersonal:
    def __init__(self, saldo):
        self.saldo = saldo

    def mostrar_info(self):
        print('---------------------------------')
        print('       [ CUENTA PERSONAL ]      ')
        print('---------------------------------')
        print(f'Saldo: ${self.saldo}')
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
            menu_principal()
        else:
            print("Opción no válida. Intente de nuevo.")
            self.mostrar_info()

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
            self.mostrar_info()

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
            self.mostrar_info()
            
        
menu_principal()
choice = input('--> ')
if choice == '1':
    cuenta = CuentaPersonal(0.0)
    cuenta.mostrar_info()
elif choice == '2':
    pass  # prestamos()
elif choice == '3':
    pass  # cuenta_luis()
elif choice == '4':
    pass  # sueldo()
elif choice == '5':
    pass  # movimientos_terceros()
else:
    print("Opción no válida. Intente de nuevo.")
    menu_principal()
    








