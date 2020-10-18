n = int(input('digite um npumero para calcular seu fatorial '))
c = n
f = 1
print('o fatorial de {}!'.format(n))
while c > 0:
    print('{} '.format(c), end='')
    print(' x 'if c > 1 else '=', end='')
    f *= c
    c -= 1
print('\no fatorial de {} é {}'.format(n, f))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break