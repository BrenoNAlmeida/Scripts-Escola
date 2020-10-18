print('''\033[34mAs fases do segundo mundo mundo de python são essas :
      '12 = condições aninhadas
      '13 = estrutura de repetição for
      '14 = estrutura de repetição while
      '15 = interrompendo repetição while\033[m''')
escolha2 = int(input('\033[31mqual fase você deseja acessar ? \033[m'))
if escolha2 == 12:
    import fase12
elif escolha2 == 13:
    import fase13
elif escolha2 == 14:
    import fase14
elif escolha2 == 15:
    import fase15
