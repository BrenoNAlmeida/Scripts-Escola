from datetime import date
atual = date.today().year
genero = str(input('Você é homem ou mulher? Digite H para HOMEM ou M para MULHER: ')).upper().strip()
if genero == 'H':
    nas = int(input('Em que ano você nasceu (ex: 1990)? '))
    ani = str(input('Este ano você já fez aniversário? Digite S para SIM ou N para NÃO: ')).upper().strip()
    if ani == 'N' or ani == 'NAO' or ani == 'NÃO':
        idade = atual - nas - 1
    else:
        idade = atual - nas
    print('Então você tem {} anos, correto?'.format(idade))
    if idade == 18:
        print('Este ano você deve se alistar no serviço militar!\n')
    elif idade < 18:
        print('Ainda falta(m) {} ano(s) para você se alistar no serviço militar!\n'.format(18 - idade))
    elif idade > 18:
        print('Já passou {} ano(s) do tempo para você se alistar no serviço militar!\n'.format(idade - 18))
elif genero == 'M':
    print('Como você é mulher, não precisará se alistar no serviço militar!\n')
else:
    print('Escolha inválida! Tente novamente.\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio39', 'r')
    print(f.read())
