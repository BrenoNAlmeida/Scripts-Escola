print('\033[1;31mvamos somar !\033[m')
n1 = int(input('\033[1;34mnumero =\033[m'))
n2 = int(input ('\033[1;34mnumero =\033[m'))
n3 = n1 + n2
print('a soma entre  \033[1;33m{}\033[m e \033[1;33m{}\033[m é igual a \033[1;32m{}'.format(n1,n2,n3))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break