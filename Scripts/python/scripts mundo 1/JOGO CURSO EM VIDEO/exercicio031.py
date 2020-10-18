distancia = float(input('Qual é a distancia da sua viagem?' ))
print('voce esta prestes a começa uma viagem de {}km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('É o preço da sua passagem sera de R${:2f}'.format(preço))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
