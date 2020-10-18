from math import hypot
co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adiacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
