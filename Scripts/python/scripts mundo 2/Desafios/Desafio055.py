maior_peso = 0
menor_peso = 1000000
for p in range(1,6):
    peso = float(input('qual o peso {}° pessoa ?  '.format(p)))
    if peso > maior_peso :
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('o maior peso é {}Kg'.format(maior_peso))
print('o menor peso é {}Kg'.format(menor_peso))