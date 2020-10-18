print('''\033[1;34mOs desafios dessa fase são esses :
         \033[32;1m 16 = Quebrando um numero
          17 = calculando a hipotenuza
          18 = Seno ,cossene tangente
          19 = Sorteando um item da lista
          20 = Sorteando uma ordem na lista
          21 = Tocando um Mp3\033[m''')
escolha3 = int(input('qual desafio você deseja ?'))
if escolha3 == 16:
    import exercicio016
elif escolha3 == 17:
    import exercicio017
elif escolha3 == 18:
    import exercicio018
elif escolha3 == 19:
    import exercicio019
elif escolha3 == 20:
    import exercicio020
elif escolha3 == 21:
    import exercicio021
