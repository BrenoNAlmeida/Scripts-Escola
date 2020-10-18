r1 = float(input('\033[1;34mprimeiro segmento = '))
r2 = float(input('\033[1;34;msegundo segmento = '))
r3 = float(input('\033[1;34;mterceiro segmento = '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32messes segmentos podem forma um triangulo\033[m')
else:
    print('\033[1;31messes segmentos NÃO podem formar um triangulo\033[m')
