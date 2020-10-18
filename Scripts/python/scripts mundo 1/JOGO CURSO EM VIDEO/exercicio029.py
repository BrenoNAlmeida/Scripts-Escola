velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! dirija com segurança!')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
