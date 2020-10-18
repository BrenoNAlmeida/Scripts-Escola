old = float(input('qual o seu ano de nascimento? '))
txp = old-1999
if old>1999:
    print('Ainda não é hora de se alistar, faltam {:.0f} anos'.format(txp))
elif old == 1999:
    print('É a hora de cortar grama, soldado.')
else:
    print('Já passou do prazo, hein, soldado?')
if old > 1999 :
    print('seu alistamento deverá ser feito em {:.0f}'.format(txp+2017))
elif old < 1999:
    print('seu alistamento deveria ter sido feito em {:.0f}'.format(txp+2017))
else:
    print('vc deve se alistar imdiatamente')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break