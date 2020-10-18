n1 = int(input('numero ='))
n2 = int(input ('numero ='))
n3 = n1 + n2
print('a soma entre  {} e {} é igual a {}'.format(n1,n2,n3))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break