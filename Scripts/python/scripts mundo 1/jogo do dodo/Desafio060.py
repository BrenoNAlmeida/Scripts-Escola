num = int(input('qual numero você deseja o fatorial ? '))
n = num
f = 1
while n > 0:
    print(' {} '.format(n), end=' ')
    print(' X ' if n > 1 else ' = ', end=' ')
    f *= n
    n -= 1
print(f)
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break