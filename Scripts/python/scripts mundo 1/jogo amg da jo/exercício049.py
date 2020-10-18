#exercício049
n = int(input('digite aqui um número inteiro: '))
print('a tabuada do número {} é:'.format(n))
for tabuada in range (1, 11):
    nn = (n*(tabuada))
    print('{} * {} = {}'.format(n, tabuada, nn))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break