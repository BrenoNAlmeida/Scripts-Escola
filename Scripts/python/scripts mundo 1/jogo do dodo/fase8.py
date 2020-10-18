print('\033[1;34mOs desafios dessa fase são esses {} : !'
          '\n\033[33;1m 16 = Quebrando um numero'
          '\n 17 = calculando a hipotenuza'
          '\n 18 = Seno ,cossene tangente'
          '\n 19 = Sorteando um item da lista'
          '\n 20 = Sorteando uma ordem na lista'
          '\n 21 = Tocando um Mp3\033[m')
desafio = int(input('qual desafio você deseja ?'))
if desafio == 16:
    import Desafio016
if desafio == 17:
    import Dsafio017
if desafio == 18:
    import Desafio018
if desafio == 19:
    import Desafio019
if desafio == 20:
    import Desafio020
if desafio == 21:
    import Desafio021
