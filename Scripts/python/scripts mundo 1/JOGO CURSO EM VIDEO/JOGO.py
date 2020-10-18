print(''' \033[35m JOGO DO CURSO EM VIDEO DE PYTHON\033[m
1  = MUNDO 1 -  FLORESTA
2  = MUNDO 2 -   GELO''')
opçao1 = 0
while opçao1 != 1 and opçao1 != 2:
    opçao1 = int(input('\033[35m QUAL MUNDO VOCÊ ESCOLHE ? [1/2] ?'))
    if opçao1 == 1:
        import MUNDO1
    if opçao1 == 2:
        import MUNDO2
