print('\033[1;34mOs desafios dessa fase são esses {} : !'
      '\n\033[33;1m 22 = Analizador de texto'
      '\n 23 = Separando digitos de um numero'
      '\n 24 = verificando as primeiras letras'
      '\n 25 = procurando uma string dentro de uma variavel'
      '\n 26 = primeira ocorrencia de uma string'
      '\n 27 = primeiro e ultimo nome de uma pessoa\033[m')
desafio = int(input('qual desafio você deseja ? '))
if desafio == 22:
    import Desafio022
if desafio == 23:
    import Desafio023
if desafio == 24 :
    import Desafio024
if desafio == 25:
    import Desafio025
if desafio == 26:
    import Desafio26
if desafio == 27:
    import Desafio027
