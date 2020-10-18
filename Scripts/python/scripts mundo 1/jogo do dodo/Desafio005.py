n1=int(input('\033[1;34mdigite um numero =\033[m'))
print('\033[1;34mO sucessor de {} é :\033[m \033[1;31m{}\033[m\n\033[1;34mO antecessor de {} é :\033[m \033[1;31m{}'.format(n1,n1+1,n1,n1-1))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break