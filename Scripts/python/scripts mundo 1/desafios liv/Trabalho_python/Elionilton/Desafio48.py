t = 0
print('Todos os números ímpares que são múltiplos de 3 e estão entre 1 e 500:')
for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        print(c, end=' ')
        t += c
print('SOMA DE TODOS: {}\n'.format(t))

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio48', 'r')
    print(f.read())
