n = int(input('Digite um número: '))
v = True

if n < 2:
    v = False
else:
    for c in range(2, n - 1):
        if n % c == 0:
            v = False

if v:
    print('{} é um número primo.\n'.format(n))
else:
    print('{} não é um número primo.\n'.format(n))

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio52', 'r')
    print(f.read())
