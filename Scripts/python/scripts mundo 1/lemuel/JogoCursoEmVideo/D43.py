peso = float(input('Digite o seu peso em Kg (ex: 80): '))
altura = float(input('Digite o seu peso em m (ex: 1.75): '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!\n')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!\n')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!\n')
elif 30 <= imc < 40:
    print('Você está com obesidade!\n')
elif imc > 40:
    print('Você está com obesidade mórbida!\n')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D43', 'r')
    print(f.read())
