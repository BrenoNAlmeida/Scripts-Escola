peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual sua altura (m) '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está de ABAIXO DO PESSO ADEQUADO')
elif 25 <= imc < 30:
    print('Voce  está em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce está em OBSIDADE!')
elif imc >= 40:
    print('Voce está em OBSIDADE MEDIA, CUIDADO!')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
