dia = input('Dia em que nasceu = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio2', 'r')
    print(f.read())
