num1 = int(input('digite um número '))
num2 = int(input('digite outro número '))
if num1 > num2:
    print('o valor maior é {}'.format(num1))
elif num2 > num1:
    print('o valor maior é {}'.format(num2))
else:
    print('não possui valores maiores, nem menores, ou seja, são iguais.')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break