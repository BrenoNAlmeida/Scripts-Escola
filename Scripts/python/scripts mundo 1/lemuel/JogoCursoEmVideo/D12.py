p = float(input('Qual é o preço do produto? '))
d = p * 0.05
r = p - d
print('O produto que custa $ {:.2f} fica por $ {:.2f} com 5% de desconto ($ {:.2f}).'.format(p, r, d), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D12', 'r')
    print(f.read())
