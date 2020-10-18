pt = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão: '))
print('\n10 Primeiros Termos da PA com Razão {} (Iniciando em {}):'.format(r, pt))
print(pt, end=' ')

for c in range(1, 10):
    pt += r
    print(pt, end=' ')
print()

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D51', 'r')
    print(f.read())
