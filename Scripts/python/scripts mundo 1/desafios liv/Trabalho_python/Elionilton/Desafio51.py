pt = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão: '))
print('\n10 Primeiros Termos da PA com Razão {} (Iniciando em {}):'.format(r, pt))
print(pt, end=' ')

for c in range(1, 10):
    pt += r
    print(pt, end=' ')
print()

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio51', 'r')
    print(f.read())
