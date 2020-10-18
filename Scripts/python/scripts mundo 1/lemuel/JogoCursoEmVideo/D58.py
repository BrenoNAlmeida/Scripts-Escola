from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 10...')
sleep(1)
numero_pensado = randint(0, 10)
quantos_chutes = 1
chute = int(input('Em qual número eu pensei? '))

while chute != numero_pensado:
    if 0 <= chute <= 10:
        if numero_pensado < chute:
            print('{}º chute errado! O número que eu pensei é menor. Chute novamente!'.format(quantos_chutes))
        else:
            print('{}º chute errado! O número que eu pensei é maior. Chute novamente!'.format(quantos_chutes))
        quantos_chutes += 1
        chute = int(input('Em qual número eu pensei? '))
    else:
        print('Chute inválido! O número que eu pensei é de 0 a 10.')
        chute = int(input('Em qual número eu pensei? '))

print('Eu pensei no número {}.'.format(numero_pensado), end=' ')
if quantos_chutes == 1:
    print('Parabéns, você acertou no 1º chute!\n')
else:
    print('Parabéns, você acertou no {}º chute!\n'.format(quantos_chutes))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D58', 'r')
    print(f.read())