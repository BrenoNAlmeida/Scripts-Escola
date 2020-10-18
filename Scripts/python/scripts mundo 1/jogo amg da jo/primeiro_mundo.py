print('''\033[34;1mAs fases do primeiro mundo de python são essas :\033[m
      \033[1;36m1 = Seja um programador
      2 = Para que serve o Python
      3 = instalando o python3 e o IDLE
      4 = primeiros comandos em python
      5 = instalando o Pycharm e o Qpython
      6 = Tipos primitivos e saida de dados
      7 = Operadores Aritmeticos
      8 = Utilizando modulos
      9 = Manipulando texto
      10 = Condições
      11 = cores no terminal\033[m''')
print('\033[35m=='*25)
escolha2 = int(input('Qual fase você deseja acessar ?'))
if escolha2== 1:
    import fase1
elif escolha2 == 2:
    import fase2
elif escolha2 == 3:
    import fase3
elif escolha2 == 4:
    import fase4
elif escolha2 == 5:
    import fase5
elif escolha2 == 6:
    import fase6
elif escolha2 == 7:
    import fase7
elif escolha2 == 8:
    import fase8
elif escolha2 == 9:
    import fase9
elif escolha2 == 10:
    import fase10
elif escolha2 == 11:
    import fase11