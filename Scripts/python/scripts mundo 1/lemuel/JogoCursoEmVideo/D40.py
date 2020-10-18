aluno = str(input('Digite o nome do(a) aluno(a): ')).title().strip()
n1 = float(input('Digite a primeira nota de {}: '.format(aluno)))
n2 = float(input('Digite a segunda nota de {}: '.format(aluno)))
m = (n1 + n2) / 2
print('A média de {} é {}!'.format(aluno, m))
if m < 5:
    print('{} foi REPROVADO(A)!\n'.format(aluno))
elif 5 <= m < 6.9:
    print('{} vai ficar de RECUPERAÇÃO!\n'.format(aluno))
elif m > 7:
    print('{} foi APROVADO(A)!\n'.format(aluno))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D40', 'r')
    print(f.read())
