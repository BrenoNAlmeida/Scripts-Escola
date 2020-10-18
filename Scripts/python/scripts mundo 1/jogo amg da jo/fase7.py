print('''\033[35;1mOs desafios dessa fase são esses :
       \033[32;1m05 = Antecessor e sucessor de um numero
       6 = Dobro , triplo e Raiz quadrada de um numero
       7 = Media aritmetica
       8 = Conversor de medidas
       9 = Tabuada de um numeno
      10 = Conversor de moedas
      11 = Pintando uma parede
      12 = Calculando desconto em 5%
      13 = Reajuste salarial
      14 = Conversor de temperaturas
      15 = Aluguel de carros\033[m''')
escolha3 = int(input('\033[31mqual desafio você deseja executar?'))
if escolha3 == 6:
    import exercicio006
elif escolha3 == 7:
    import exercicio007
elif escolha3 == 8:
    import exercicio008
elif escolha3 == 9:
    import exercicio009
elif escolha3 == 10:
    import exercicio010
elif escolha3 == 11:
    import exercicio011
elif escolha3 == 12:
    import exercicio012
elif escolha3 == 13:
    import exercicio013
elif escolha3 == 14:
    import exercicio014
elif escolha3 == 15:
    import exercicio015
