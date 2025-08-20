print('Welcome to the Sorting Hat!')
gryf = 0
rav = 0
huf = 0
sly = 0
op = int(input('Q1) Do you like Dawn or dusk?\n    1) Dawn\n    2) Dusk\n  -> '))
if op == 1:
    gryf = 1
    rav = 1
else:
    huf = 1
    sly = 1

op = int(input('Q2) When Im dead, I want people to remember me as:\n    1) The Good\n    2) The Great\n    3) The Wise\n    4) The Bold\n  -> '))
if op == 1:
    huf += 2
elif op == 2:
    sly += 2
elif op == 3:
    rav += 2
else:
    gryf += 2

op = int(input('Q3) Which kind of instrument most pleases your ear?\n    1) The violin\n    2) The trumpet\n    3) The piano\n    4) The drum\n  -> '))
if op == 1:
    sly += 4
elif op == 2:
    huf += 4
elif op == 3:
    rav += 4
else:
    gryf += 4

if gryf > huf and gryf > rav and gryf > sly:
    print('You belong in Gryffindor!')
elif huf > gryf and huf > rav and huf > sly:
    print('You belong in Hufflepuff!')
elif rav > gryf and rav > huf and rav > sly:
    print('You belong in Ravenclaw!')
else:
    print('You belong in Slytherin!')
