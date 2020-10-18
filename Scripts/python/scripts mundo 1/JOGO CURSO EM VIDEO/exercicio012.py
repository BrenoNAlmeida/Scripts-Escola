preço = float(input('Qual é o valor do produto? R$'))
novo = preço - (preço * 5 / 100)
print('0 valor que custava R${:.2f}, na promoção com descoto de 5% vai custar R${:.2f}'.format(preço, novo))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
