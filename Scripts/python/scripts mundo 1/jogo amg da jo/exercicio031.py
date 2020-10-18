d=float(input('qual a distancia da sua viagem em Km ?'))
n=d*0.50
de=d*0.45
if d <= 200:
    print('a viagem vai custar R${}'.format(n))
else:
    print('a viagem custará R${}'.format(de))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break