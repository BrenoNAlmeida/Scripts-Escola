import time
import random
print('\033[;31m#\033[m'*28)
print('É JOKEMPÔ QUE VOCÊ QUER, @?\nENTÃO TXOMA')
print('\033[;31m#\033[m'*28)
itens = ('pedra', 'papel', 'tesoura')
print('''Olhe, @, você tem 3 escolhas:
    pedra [ 1 ]
    papel [ 2 ]
    tesoura [ 3 ]''')
es = random.randint(0,2)
ef = random.randint(0,2)
ent = str(input('Escolha um digite aqui, @ ')).strip()
print('''    JO
    KEN
    PO''')
time.sleep(1)
print('=-'*18)
print('o jogador escolheu {}'.format(itens[ef]))
print('o computador escolheu {}'.format(itens[es]))
print('-='*18)
'''if'''

'''if 1 == ent and 2 == es and ef == 1:
    print('PERDEU, BB')
elif 1 == ent and 3 == es and ef 1:
    print('AEEEE, GANHOU')
elif 2 == ent and 1 == es:
    print('AEEE, GANHOU, @')
elif 2 == ent and 3 == es:
    print('PERDEU, BB')
elif 3 == ent and 1 == es:
    print('perdeu, bb')'''
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break