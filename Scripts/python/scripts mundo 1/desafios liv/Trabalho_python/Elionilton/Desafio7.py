nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
media = (nt1 + nt2) / 2
print('A primeira nota foi {}, a segunda nota foi {} e a média entre elas é {}.'.format(nt1, nt2, media), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio7', 'r')
    print(f.read())
