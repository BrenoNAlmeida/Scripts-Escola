salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    novo_salario = (salario * 0.10) + salario
    print('O salário atual de R$ {:.2f} aumentou em 10% (R$ {:.2f}),'.format(salario, salario * 0.10), end=' ')
    print('totalizando R$ {:.2f}!'.format(novo_salario), "\n")
else:
    novo_salario = (salario * 0.15) + salario
    print('O salário atual de R$ {:.2f} aumentou em 15% (R$ {:.2f}),'.format(salario, salario * 0.15), end=' ')
    print('totalizando R$ {:.2f}!'.format(novo_salario), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio34', 'r')
    print(f.read())