
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
        prestamos()
    elif choice == '3':
        cuenta_luis()
    elif choice == '4':
        sueldo()
    elif choice == '5':
        movimientos_terceros()
    else:
        print("Opción no válida. Intente de nuevo.")
        menu_principal()


    
    