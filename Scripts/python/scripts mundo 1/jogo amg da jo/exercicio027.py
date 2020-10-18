nome=str(input('digite seu nome completo =')).split()
print('seu primeiro nome é {}'.format(nome[0]))
print('e seu ultimo nome é {}'.format(nome[len(nome)-1] ))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break