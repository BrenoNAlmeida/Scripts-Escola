''' from math import trunc
num = float(input('Digite um valor: '))
print('0 valor digitado foi {} e sua porção inteira será {}'.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print('0 valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
