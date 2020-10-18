n=int(input('digite um numero : '))
ra=n**(1/2)
print('O dobro de {} é :{}\nO triplo de {} é :{}'.format(n,n*2,n,n*3))
print('A raiz quadrada de {} é : {}'.format(n,ra))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break