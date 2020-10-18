n = float(input('Digite um Número Real (ex: 6.127): '))
nr = int(n)
print('O número inteiro de {} é {}!'.format(n, nr), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D16', 'r')
    print(f.read())
