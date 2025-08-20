print('===========================')
print('  CALCULATOR APP PROGRAM')
print('===========================')
print('Choose your figure: \n')
choice = int(input('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n--> '))
while choice != 5:
    if choice == 1: 
        base = float(input('Enter the base of the triangle: '))
        height = float(input('Enter the height of the triangle: '))
        area = (base * height) / 2
        print(f'The area of the triangle is: {area}')
        print('===========================')
        choice = 5
    elif choice == 2:
        length = float(input('Enter the length of the rectangle: '))
        width = float(input('Enter the width of the rectangle: '))
        area = length * width
        print(f'The area of the rectangle is: {area}')
        print('===========================')
        choice = 5
    elif choice == 3:
        side = float(input('Enter the side length of the square: '))
        area = side ** 2
        print(f'The area of the square is: {area}')
        print('===========================')
        choice = 5
    elif choice == 4:
        radius = float(input('Enter the radius of the circle: '))
        area = 3.14159 * radius ** 2
        print(f'The area of the circle is: {area}')
        print('===========================')
        choice = 5

print('Thank you for using the calculator app!')