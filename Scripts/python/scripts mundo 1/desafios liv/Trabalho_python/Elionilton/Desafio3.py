n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
re = n1 + n2
print('A soma é', re, "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio3', 'r')
    print(f.read())
