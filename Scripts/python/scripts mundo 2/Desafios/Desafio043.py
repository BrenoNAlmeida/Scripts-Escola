print('\033[034m vamos calcular seu IMC ')
vou_matar_alguem = float(input('Qual a sua massa em Kg ?'))
acho_que_eu_mesmo = float(input('Qual a sua altura em metros ?'))
odeio_isso = vou_matar_alguem // (acho_que_eu_mesmo **2)
if odeio_isso < 18.6:
    print(' seu IMC é {} você esta abaixo do peso'.format(odeio_isso))
elif odeio_isso < 20.1:
    print('seu IMC é {} você esta no peso ideal'.format(odeio_isso))
elif odeio_isso < 30.1:
    print('seu IMC é {} você esta sobrepeso'.format(odeio_isso))
elif odeio_isso < 40.1:
    print('seu IMC é {} você esta obeso'.format(odeio_isso))
else:
    print('seu IMC é {} você esta em obesidade mórdida'.format(odeio_isso))

