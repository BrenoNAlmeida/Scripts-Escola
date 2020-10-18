#exercício070
nome = 0
pre = 0
con = 1
cont = 0
mais = 1000
c = 0
menos = 0
f = ''
while True:
    nome = str(input('Nome do produto: '))
    pre = float(input('Qual o preço R$'))
    cont += pre
    if pre > mais:
        c += 1
    if menos == 0:
        menos = pre
        f = nome
    if pre <= menos:
        menos = pre
        f = nome
    con = int(input('Continuar?\n[ 1 ] - sim\n[ 2 ] - não'))
    if con == 2:
        break
print('O total gasto na compra foi {} reais.'.format(cont))
if c == 0:
    print('Não tem nenhum produto superior a 1000 reais')
if c == 1:
    print('apenas um produto é superior a 1000 reais')
if c > 1:
    print('{} produtos tem preços superiores a mil reais, rico'.format(c))
print('o menor preço foi: {} reais e foi {}'.format(menos, f))
