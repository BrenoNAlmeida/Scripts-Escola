num = int(input('Digite um número inteiro (ex: 55): '))
if num % 2 == 0:
    print('{} é um número par!'.format(num), "\n")
else:
    print('{} é um número ímpar!'.format(num), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio30', 'r')
    print(f.read())