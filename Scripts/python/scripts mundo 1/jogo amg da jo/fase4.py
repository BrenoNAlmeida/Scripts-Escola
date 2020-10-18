print('''\033[33;1mOs desafios dessa fase são esses :
1 = Deixando tudo pronto
2 = Respondendo ao usuario\033[m''')
escolha3 = int(input('qual desafio você deseja executar ? '''))
if escolha3 == 1:
    import exercicio001
if escolha3 == 2:
    import exercicio002
