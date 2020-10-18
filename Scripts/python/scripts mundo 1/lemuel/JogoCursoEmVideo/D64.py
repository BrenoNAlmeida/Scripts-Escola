n = int(input('Digite um número qualquer (ou digite 999 para encerrar o programa): '))
if n != 999:
    numeros = 1
    soma = n
else:
    numeros = 0
    soma = 0

while n != 999:
    n = int(input('Digite um número qualquer (ou digite 999 para encerrar o programa): '))
    if n != 999:
        soma += n
        numeros += 1

if numeros == 0:
    print('Você não digitou nenhum número.\n')
elif numeros == 1:
    print('Você digitou somente o número {}.\n'.format(soma))
else:
    print('Você digitou {} números. A soma total deles é {}.\n'.format(numeros, soma))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D64', 'r')
    print(f.read())