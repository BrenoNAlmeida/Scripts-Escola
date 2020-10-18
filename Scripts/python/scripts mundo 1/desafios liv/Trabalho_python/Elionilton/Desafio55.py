maior = -10 ** 20
menor = 10 ** 20
for c in range(1, 5 + 1):
    msg = 'Digite o peso da pessoa Nº {}: '.format(c)
    peso = float(input(msg))
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso

print('Menor peso: {:.2f} kg\nMaior peso: {:.2f} kg\n'.format(menor, maior))

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio55', 'r')
    print(f.read())
