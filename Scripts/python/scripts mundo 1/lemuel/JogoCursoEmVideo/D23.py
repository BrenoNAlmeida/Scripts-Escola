n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('\nUnidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D23', 'r')
    print(f.read())