from math import sqrt
c1=float(input('cateto oposto = '))
c2=float(input('cateto adjacente ='))
H= sqrt (c1**2 + c2**2)
print ('o valor da hipotenusa é {:.3}'.format(H))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break