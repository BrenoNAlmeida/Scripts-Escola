print('É sequÊncia de Fibaccioni que você quer?')
ter = int(input('quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{}...{}...'.format(t1, t2), end='')
c = 3
while c <= ter:
    t3 = t1+ t2
    print('{}...'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('\nfim')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
