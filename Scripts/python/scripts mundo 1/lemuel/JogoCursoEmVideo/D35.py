r1 = float(input('Digite um número para o valor da primeira reta: '))
r2 = float(input('Digite um número para o valor da segunda reta: '))
r3 = float(input('Digite um número para o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {} x {} x {} podem formar um triângulo!'.format(r1, r2, r3), "\n")
else:
    print('As retas {} x {} x {} não podem formar um triângulo!'.format(r1, r2, r3), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D35', 'r')
    print(f.read())
