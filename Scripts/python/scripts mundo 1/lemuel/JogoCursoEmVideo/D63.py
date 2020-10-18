contador = 1
x = 1
y = 0

n = int(input('Digite quantos primeiros elementos da Sequência de Fibonacci você quer exibir: '))

if n > 0:
    if n == 1:
        print('0')
    else:
        print('0', end=' → ')

    while contador < n:
        z = x + y
        if contador == n - 1:
            print(z, end='')
        else:
            print(z, end=' → ')
        x = y
        y = z
        contador += 1
print()

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D63', 'r')
    print(f.read())

