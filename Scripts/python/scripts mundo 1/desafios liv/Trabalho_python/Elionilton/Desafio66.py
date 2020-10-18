s = t = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    t += 1
if t == 0:
    print('Você não digitou nenhum valor!\n')
elif t == 1:
    print(f'Você digitou somente 1 valor, portanto seu total é {s}!\n')
else:
    print(f'A soma dos {t} valores foi {s}!\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio66', 'r')
    print(f.read())