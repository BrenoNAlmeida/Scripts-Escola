from datetime import date
ano = date.today().year
pessoas = 0

for c in range(1, 7 + 1):
    msg = 'Digite o ano de nascimento da pessoa Nº {}: '.format(c)
    data = int(input(msg))
    if ano - data >= 21:
        pessoas += 1

if pessoas == 0:
    print('Todas as 7 pessoas ainda são menores de idade.\n')
elif pessoas == 1:
    print('6 pessoas ainda são menores de idade. Somente 1 já atingiu a maioridade.\n')
else:
    print('Das 7 pessoas, {} são menores de idade e {} já atingiram a maioridade.\n'.format(7 - pessoas, pessoas))

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio54', 'r')
    print(f.read())
