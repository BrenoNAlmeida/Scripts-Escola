sexo = str(input('digite o seu sexo [F/M] ')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sesxo [F/M]'))
print('seu sexo, {}, foi registrado com sucesso'.format(sexo))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break