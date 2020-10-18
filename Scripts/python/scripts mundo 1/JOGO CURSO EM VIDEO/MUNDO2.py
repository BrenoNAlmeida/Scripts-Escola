print('''\033[35m ESSAS SÃO AS FASES DO MUNDO 2 :
      [12] - condições aninhadas
      [13] - estrutura de repetição for
      [14] - estrutura de repetição while
      [15] - interrompendo repetição while\033[m''')
opçao2 = 12
while opçao2 > 11:
    opçao2 = int(input('\033[35m QUAL FASE VOCê ESCOLHE ?'))
    if opçao2 == 12:
        import fase12
    elif opçao2 == 13:
        import fase13
    elif opçao2 == 14:
        import fase14
    elif opçao2 == 15:
        import fase15
