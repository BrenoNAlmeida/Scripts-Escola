dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('0 total a pagar é de R${:.2f}'.format(pago))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
