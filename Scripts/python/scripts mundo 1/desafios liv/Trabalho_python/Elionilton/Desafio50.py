t = 0
np = 0

for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        t += n
        np += 1

if np == 0:
    print('Você não digitou nenhum número par, portanto, o seu total é 0.\n')
elif np == 1:
    print('Você digitou {} número par. O seu total é {}.\n'.format(np, t))
else:
    print('Você digitou {} números pares. A soma total deles é {}.\n'.format(np, t))

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio50', 'r')
    print(f.read())
