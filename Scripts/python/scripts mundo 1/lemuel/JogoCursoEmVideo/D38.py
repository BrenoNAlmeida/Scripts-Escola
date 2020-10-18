n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 == n2:
    print('{} e {} são números exatamente iguais!\n'.format(n1, n2))
elif n1 > n2:
    print('{} é maior do que {}!\n'.format(n1, n2))
elif n1 < n2:
    print('{} é menor do que {}!\n'.format(n1, n2))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D38', 'r')
    print(f.read())
