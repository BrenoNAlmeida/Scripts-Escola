n=int(input('\033[4;31mA tabuada de qual numero você deseja ?\033[m'))
print('\033[32m==\033[m'*19)
n1=n*1
n2=n*2
n3=n*3
n4=n*4
n5=n*5
n6=n*6
n7=n*7
n8=n*8
n9=n*9
n10=n*10
print('\033[4;31mA tabuada de {} é respectivamente :\033[m'.format(n))
print('\033[34m1 X {} = {}\n2 X {} = {}\n3 X {} = {}'.format(n,n1,n,n2,n,n3))
print('4 X {} = {}\n5 X {} = {}\n6 X {} = {}'.format(n,n4,n,n5,n,n6))
print('7 X {} = {}\n8 X {} = {}\n9 X {} = {}'.format(n,n7,n,n8,n,n9))
print('10 X {} = {}'.format(n,n10))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break