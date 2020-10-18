from math import hypot
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
r = hypot(c1, c2)
print('O comprimento da hipotenusa é {}!'.format(r), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D17', 'r')
    print(f.read())
