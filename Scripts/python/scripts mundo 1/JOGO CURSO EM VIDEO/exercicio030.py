numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('0 numero {} é PAR'.format(numero))
else:
    print('0 numero {} é IMPAR'.format(numero))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
