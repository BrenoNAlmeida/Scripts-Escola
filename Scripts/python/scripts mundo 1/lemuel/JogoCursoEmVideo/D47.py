print('Todos os números pares entre 1 e 50:')
for c in range(2, 50 + 1, 2):
    print(c, end=' \n')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D47', 'r')
    print(f.read())
