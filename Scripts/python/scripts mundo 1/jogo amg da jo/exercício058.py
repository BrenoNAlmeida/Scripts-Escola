import random
from time import sleep
c = 0
num = random.randint(1, 10)
nume = int(input('''tente advinhar o número que o computador pensou,
[ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ][ 8 ][ 9 ][ 10 ]
digite-o aqui '''))
sleep(1)
print('PROCESSANDO...')
while nume != num:
    nume = int(input('''ERROU. tente novamente:
    [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ][ 8 ][ 9 ][ 10 ]
    digite-o aqui '''))
    c += 1
print('parabéns, você conseguiu acertar!')
if c == 0:
    print('fim')
elif c == 1:
    print('Você ocnseguiu com {} tentativa'.format(c))
else:
    print('você conseguiu com {} tentativas'.format(c))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break