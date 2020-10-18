from time import sleep
print('\033[;34m=-\033[m'*12)
print('\033[1m          IMC')
print('\033[;34m=-\033[m'*12)
peso = float(input('qual o seu peso? '))
altt = float(input('qual a sua altura? '))
imc = ((peso)/altt**2)
print('calculando')
sleep(2)
print('seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('abaixo do ideal')
elif imc > 18.5 or imc == 18.5:
    if imc < 25:
        print('normal')
elif imc >25 or imc == 25:
    if imc < 30 or imc == 30:
        print('sobre peso')
if imc >30:
    if imc <40 or imc ==40:
        print('obesidade')
elif imc > 40:
    print('obesidade mórbida')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break