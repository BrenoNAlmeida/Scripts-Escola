from time import sleep
valor = float(input('digite aqui o valor '))
pay = int(input('''escolha uma forma de pagamento:
 [ 1 ] a vista/ cheque
 [ 2 ] a vista no cartão
 [ 3 ] em até 2x no cartão
 [ 4 ] 3x ou mais no cartão...
   qual?  '''))
fiv = ((valor) - (5*valor/100))
tend = ((valor) - (10*valor/100))
jur = (120*valor/100)
print('calculando')
sleep(1)
if pay == 1:
    print('valor final {} reais'.format(tend ))
elif pay == 2:
    print('o valor final é {} reais'.format(fiv))
elif pay == 3:
    print('o valor final é {} reais'.format(valor))
elif pay == 4:
    print('o valor final será {} reais'.format(jur))
else:
    print('opção inválida')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break