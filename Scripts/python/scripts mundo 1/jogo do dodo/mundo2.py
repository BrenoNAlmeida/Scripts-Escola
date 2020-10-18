print('\033[34mAs fases desses mundo são essas :\n'
      '12 = condições aninhadas\n'
      '13 = estrutura de repetição for\n'
      '14 = estrutura de repetição while\n'
      '15 = interrompendo repetição while\033[m\n')
fase = int(input('\033[31mqual fase você deseja pequeno gafanhoto ? \033[m'))
if fase == 12:
    import fase12
if fase == 13:
    import fase13
if fase == 14:
    import fase14
if fase == 15:
    import fase15
