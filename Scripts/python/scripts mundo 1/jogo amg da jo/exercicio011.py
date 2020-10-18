h=float(input('qual a altura da parede ?'))
l=float(input('qual a largura da parede ?'))
a=h*l
qt=a/2
print('A área da sua parede é de : {} m² '.format(a))
print('A quantidade de tinta necessaria será : {:.2} litros'.format(qt))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break