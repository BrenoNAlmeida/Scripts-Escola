print('Todos os números pares entre 1 e 50:')
for c in range(2, 50 + 1, 2):
    print(c, end=' \n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio47', 'r')
    print(f.read())
