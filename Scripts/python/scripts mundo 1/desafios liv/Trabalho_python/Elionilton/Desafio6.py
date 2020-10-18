n = int(input('Digite um número: '))
print('O número digitado foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {}.'.format(n, n * 2, n * 3, n ** (1/2)), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio6', 'r')
    print(f.read())
