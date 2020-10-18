n1=int(input('digite um numero ='))
print('O sucessor de {} é : {}\nO antecessor de {} é : {}'.format(n1,n1+1,n1,n1-1))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break