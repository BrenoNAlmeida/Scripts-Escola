from datetime import date
atual = date.today().year
nas = int(input('Em que ano o atleta nasceu (ex: 1990)? '))
ani = str(input('Este ano o atleta já fez aniversário? Digite S para sim ou N para não: ')).upper().strip()
if ani == 'N' or ani == 'NAO' or ani == 'NÃO':
    idade = atual - nas - 1
else:
    idade = atual - nas
if idade <= 9:
    print('O atleta de {} anos vai ficar na categoria MIRIM!\n'.format(idade))
elif idade <= 14:
    print('O atleta de {} anos vai ficar na categoria INFANTIL!\n'.format(idade))
elif idade <= 19:
    print('O atleta de {} anos vai ficar na categoria JUNIOR!\n'.format(idade))
elif idade <= 25:
    print('O atleta de {} anos vai ficar na categoria SÊNIOR!\n'.format(idade))
elif idade > 25:
    print('O atleta de {} anos vai ficar na categoria MASTER!\n'.format(idade))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D41', 'r')
    print(f.read())
