print('''\033[1;34mOs desafios dessa fase são esses :
      \033[32;1m 22 = Analizador de texto
      23 = Separando digitos de um numero
      24 = verificando as primeiras letras
      25 = procurando uma string dentro de uma variavel
      26 = primeira ocorrencia de uma string
      27 = primeiro e ultimo nome de uma pessoa\033[m''')
escolha3 = int(input('qual desafio você deseja executar ? '))
if escolha3 == 22:
    import exercicio022
elif escolha3== 23:
    import exercicio023
elif escolha3 == 24 :
    import exercicio024
elif escolha3 == 25:
    import exercicio025
elif escolha3 == 26:
    import exercicio26
elif escolha3 == 27:
    import exercicio027
