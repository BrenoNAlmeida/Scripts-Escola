s=float(input('\033[1mquanto é o seu salario ?\033[m'))
a1=(s*10)/100
a2=(s*15)/100
if s >= 1250.00:
    print ('\033[1;34mseu almento sera de {}\033[m'.format(a1))
else:
    print('\033[1;31mseu almento sera de {}\033[m'.format(a2))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break