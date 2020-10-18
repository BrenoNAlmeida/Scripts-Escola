print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{}...{}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('... {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print('Acabou, tá?..')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break