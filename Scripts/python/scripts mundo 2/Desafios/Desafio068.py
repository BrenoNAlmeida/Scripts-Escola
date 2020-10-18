#exercício068 #teamamos,Dodo
desg = '-'
print(f'{desg *35}\n  É PAR OU ÍMPAR QUE VC QUER, @?\n{desg *35}')
import random
cont = 0
sorte = 0
while True:
    sorte = int(input('[ 1 ] - PAR\n[ 2 ] - ÍMPAR'))
    ni = int(input('escolha um número entre 0 e 10 '))
    num = random.randint(0,9)
    print('o computador escolheu {} e você {}'.format(num, ni))
    par = (ni+num) % 2
    if sorte == 1:
        if par != 0:
            break
    if sorte == 2:
        if par == 0:
            break
    cont += 1
    print('GANHOU, GAFANHOTO!')
print(f'VOCÊ PERDEU, GAFANHOTO')
if cont == 0:
    print(end='')
else:
    print(f'Você teve {cont} vitórias consecultivas, gafanhoto, PARABÉNS!')


