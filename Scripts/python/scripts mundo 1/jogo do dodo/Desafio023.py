num=int(input('digite um numero ='))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('a unidade é = {}\na dezena é = {}'.format(u,d))
print('a centena é = {}\na milhar é = {}'.format(c,m))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break