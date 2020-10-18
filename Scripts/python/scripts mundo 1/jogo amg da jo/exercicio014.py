print('converta as temperaturas de °C em °F')
print('=='*18)
c = float(input('informe a temperatura em °C = '))
f = ((9 * c) / 5) + 32
print('A temperatura {}°C é igual a {}°F'.format(c, f))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break