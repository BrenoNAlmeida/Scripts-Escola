s = float(input('Qual é o salário do funcionário? '))
a = s * 0.15
r = s + a
print('O salário atual é $ {:.2f}, e com o aumento de 15% ($ {:.2f}) ficará $ {:.2f}!'.format(s, a, r), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D13', 'r')
    print(f.read())