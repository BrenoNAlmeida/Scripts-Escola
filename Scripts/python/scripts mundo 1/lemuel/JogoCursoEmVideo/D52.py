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

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D52', 'r')
    print(f.read())
