d=float(input('qual a distancia da sua viagem em Km ?'))
n=d*0.50
de=d*0.45
if d <= 200:
    print('a viagem vai custar R${}'.format(n))
else:
    print('a viagem custará R${}'.format(de))
