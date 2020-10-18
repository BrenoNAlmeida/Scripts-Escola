print('vamos ver se o ano é bissexto !')
ano=int(input('Digite um ano ='))
an1=ano%4
an2=ano%400
if an1 and an2 != 0:
     print('o ano {} não é bissexto !'.format(ano))
else:
     print('o ano {} é bissexto'.format(ano))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break