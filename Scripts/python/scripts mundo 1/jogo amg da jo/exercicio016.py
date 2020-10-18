n1=float(input("Digite um numero = "))
n2=int(n1)
print('A parte inteira de {:.3f} é igual a {}'.format(n1 , n2 ))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break