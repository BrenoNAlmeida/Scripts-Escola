real = float(input('Quanto dinheiro você recebeu do seu irmão? R$'))
dolar = real /3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
