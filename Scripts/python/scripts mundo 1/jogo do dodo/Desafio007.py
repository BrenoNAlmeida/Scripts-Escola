print('      \033[4;31mCalcule a sua media anual\033[m     ')
n1=float(input('\033[34;1mnota do primeiro bimestre ='))
n2=float(input('nota do segundo bimestre = '))
n3=float(input('Nota do terceiro bimestre = '))
n4=float(input('Nota do quarto bimestre = \033[m'))
m=(n1+n2+n3+n4)/4
print('\033[1;32mA sua media é de :\033[m \033[31m{}'.format(m))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break