print('\033[32m BEM VINDO A BIBLIOTECA DO CURSO EM VIDEO DE PYTHON\033[m')
print('''[ 1 ] - MUNDO 1 -  FLORESTA
[ 2 ] - MUNDO 2 -   GELO''')
escolha1 = int(input('Qual mundo você deseja acessar [1/2] ?'))
if escolha1 == 1:
    import primeiro_mundo
if escolha1 == 2:
    import segundo_mundo