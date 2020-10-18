print('''\033[35m ESSAS SÃO AS FASES DO MUNDO 1 :\033[m
      \033[1;36m[1] = Seja um programador
      [2] - Para que serve o Python
      [3] - instalando o python3 e o IDLE
      [4] - primeiros comandos em python
      [5] - instalando o Pycharm e o Qpython
      [6] - Tipos primitivos e saida de dados
      [7] - Operadores Aritmeticos
      [8] - Utilizando modulos
      [9] - Manipulando texto
      [10] - Condições
      [11] - cores no terminal\033[m''')
opçao2 = 12
while opçao2 > 11:
    opçao2 = int(input('\033[35m QUAL FASE VOCê ESCOLHE ?'))
    if opçao2 == 1:
        import fase1
    elif opçao2 == 2:
        import fase2
    elif opçao2 == 3:
        import fase3
    elif opçao2 == 4:
        import fase4
    elif opçao2 == 5:
        import fase5
    elif opçao2 == 6:
        import fase6
    elif opçao2 == 7:
        import fase7
    elif opçao2 == 8:
        import fase8
    elif opçao2 == 9:
        import fase9
    elif opçao2 == 10:
        import fase10
    elif opçao2 == 11:
        import fase11