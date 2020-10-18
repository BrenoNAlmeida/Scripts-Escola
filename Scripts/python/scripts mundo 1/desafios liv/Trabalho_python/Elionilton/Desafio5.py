n = int(input('Digite um número: '))
print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}.'.format(n, n-1, n+1), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio5', 'r')
    print(f.read())

