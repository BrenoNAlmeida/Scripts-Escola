c = float(input('Digite a temperatura em ºC: '))
f = (9 * (c / 5)) + 32
print('{:.1f}ºC é igual a {:.1f}ºF!'.format(c, f), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D14', 'r')
    print(f.read())
