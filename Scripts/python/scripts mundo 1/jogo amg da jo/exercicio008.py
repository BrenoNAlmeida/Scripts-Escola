n=float(input('digite a quantidade de metros ='))
c=n*100
m=n*1000
print('O valor em centimetros é : {}\nO valor em milímetros é : {}'.format(c,m))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break