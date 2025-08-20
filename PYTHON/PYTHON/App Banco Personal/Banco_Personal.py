
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
    
menu_principal()
choice = input('--> ')
    if choice == '1':
        cuenta_personal()
    elif choice == '2':
        #prestamos()
    elif choice == '3':
       # cuenta_luis()
    elif choice == '4':
        #sueldo()
    elif choice == '5':
        #movimientos_terceros()
    else:
        print("Opción no válida. Intente de nuevo.")
        menu_principal()

class CuentaPersonal:
    def __init__(self):
        self.saldo = 0

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





#def cuenta_personal():
    print('---------------------------------')
    print('       [ CUENTA PERSONAL ]      ')
    print('---------------------------------')
    print('Saldo: $')
    print('---------------------------------')
    print('1) Depositar')
    print('2) Retirar')
    print('3) Volver al menú principal')
    sub_choice = input('--> ')
    if sub_choice == '1':
        depositar()
    elif sub_choice == '2':
        retirar()
    elif sub_choice == '3':
        menu_principal()
    else:
        print("Opción no válida. Intente de nuevo.")
        cuenta_personal()

#def depositar():
    print('---------------------------------')
    print('       [ DEPOSITAR ]            ')
    print('---------------------------------')
    print('Ingrese el monto a depositar: ')
    monto = float(input('--> '))
    if monto <= 0:
        print("El monto debe ser mayor a cero.")
        depositar()
    else:
        # Aquí se actualizaría el saldo de la cuenta personal
        
        print(f'Se han depositado ${monto} en su cuenta.')
        cuenta_personal()