n = 0
d = 0
r = 0
g = 1
n = int(input('digite um número aqui '))
f = n
cont = int(input('''Você quer mesmo continuar, @??
[ 1 ] - Sim
[ 2 ] - Não '''))
while cont == 1:
    n = int(input('digite um número aqui rs '))
    cont = int(input('''Você quer mesmo continuar, @??
    [ 1 ] - Sim
    [ 2 ] - Não '''))
    d += n
    g += 1
    if f < n:
        r = f
    else:
        r = n
if d == 0:
    r = f
med = (d + f)/(g)
print('a média dos números foi {:0.1f} rs'.format(med))
if med == n and g != 1:
    print('Todos os números são igauis ;)')
if med == n and d == 0:
    print('apenas um valor, hein, gafanhoto? então o menor é ele mesmo rs: {}'.format(f))
else:
    print('o menor número foi: {}'.format(r))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
