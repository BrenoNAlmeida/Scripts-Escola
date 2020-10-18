r = float(input('Quanto dinheiro em Reais você tem? '))
d = 3.27
print('\nA cotação do Dólar está a R$ {:.2f} hoje. Com R$ {:.2f}, você consegue comprar U$ {:.2f}!'.format(d, r, r / d), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D10', 'r')
    print(f.read())
