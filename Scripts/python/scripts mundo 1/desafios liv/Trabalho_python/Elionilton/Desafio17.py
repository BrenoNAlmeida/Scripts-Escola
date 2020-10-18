from math import hypot
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
r = hypot(c1, c2)
print('O comprimento da hipotenusa é {}!'.format(r), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio17', 'r')
    print(f.read())
