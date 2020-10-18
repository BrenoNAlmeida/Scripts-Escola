ano = int(input('Digite um ano (ex: 1997): '))
tam = len(str(ano))
if ano % 4 == 0:
    if str(ano)[tam - 1] == '0':
        if str(ano)[tam - 2] == '0':
            if ano % 400 == 0:
                print('{} é um ano bissexto!'.format(ano), "\n")
            else:
                print('{} não é um ano bissexto!'.format(ano), "\n")
        else:
            print('{} é um ano bissexto!'.format(ano), "\n")
    else:
        print('{} é um ano bissexto!'.format(ano), "\n")
else:
    print('{} não é um ano bissexto!'.format(ano), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio32', 'r')
    print(f.read())