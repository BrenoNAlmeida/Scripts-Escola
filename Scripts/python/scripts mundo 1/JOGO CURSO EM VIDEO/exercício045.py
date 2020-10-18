from  random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' Suas opções:)
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
Jogador = int(input('Qual é sua jogada ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[Jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if Jogador == 0:
        print('EMPATOU!')
    elif Jogador == 1:
        print('JOGADOR VENCEU!')
    elif Jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INAVALIDA!')
elif computador == 1: # computador jogou PAPEL
    if Jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif Jogador == 1:
        print('EMPATOU!')
    elif Jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INAVALIDA!')
elif computador == 2: # computador jogou TESOURA
    if Jogador == 0:
        print('JOGADOR VENCEU!')
    elif Jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif Jogador == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INAVALIDA!')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
