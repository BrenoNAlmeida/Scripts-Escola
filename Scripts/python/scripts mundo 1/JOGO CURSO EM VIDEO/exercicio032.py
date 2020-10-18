ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0:
   print('0 ano {} é BISSEXTO'.format(ano))
else:
    print('0 ano {} NÃO é BISSEXTO'.format(ano))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
