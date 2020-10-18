print('''\033[1;34mOs desafios dessa fase são esses {} : !
       28 = jogo do adivinha
       29 = Radar eletronico
       30 = Par ou impar
       31 = custo da viagem
       32 = Ano bissexto
       33 = Maior e menor valor
       34 = Almento de salario
       35 = Analizando triangulo\033[32m''')
escolha3 = int(input('qual desafio você deseja ? '))
if escolha3 == 28:
    import exercicio028
elif escolha3 == 29:
    import exercicio029
elif escolha3 == 30:
    import exercicio030
elif escolha3 == 31:
    import exercicio031
elif escolha3 == 32:
    import exercicio032
elif escolha3 == 33:
    import exercicio033
elif escolha3 == 34:
    import exercicio034
elif escolha3 == 35:
    import exercicio035
