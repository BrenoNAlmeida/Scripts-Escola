n=int(input('digite um numero ='))
an=n%2
if an == 0:
    print('O numero {} é PAR'.format(n))
else:
    print('o numero {} é IMPAR'.format(n))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break