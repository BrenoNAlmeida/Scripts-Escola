c = 0
d = 0
n = int(input('digite um número qualquer\n para parar digite 999 '))
z = n
while n != 999:
    n = int(input('digite um número qualquer rs \n para parar digite ''999'' '))
    c += n
    d += 1
if d == 0 :
    print('fim')
else:
    print('foram apresentados {} números'.format(d))
    print('a soma é {}'.format(c - 999 + z))
    print('fim')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break