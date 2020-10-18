print('      Calcule a sua media anual     ')
n1=float(input('nota do primeiro bimestre ='))
n2=float(input('nota do segundo bimestre = '))
n3=float(input('Nota do terceiro bimestre = '))
n4=float(input('Nota do quarto bimestre = '))
m=(n1+n2+n3+n4)/4
print('A sua media é de : {}'.format(m))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break