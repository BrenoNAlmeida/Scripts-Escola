print('-=-'*20)
print('ANALISANDO TRIÂNGULOS...')
print('-=-'*20)
a = float(input('diite aqui o comprimento de um lado '))
b = float(input('digite aqui o valor de outro lado '))
c = float(input('digite aqui o valor de outro lado '))
if a <0:
    a = a*-1
if b <0:
    b  = b*-1
if c <0:
    c = c*-1
if a<c+b and b<a+c and c<a+b:
        print('sim, é POSSÍVEL formar um triângulo.')
else:
    print('NÃO é possível formar um triângulo.')
if a == b and b == c:
    if a == c:
        print('EQUILÁTERO')
elif a == b or a == c or b == c:
    print('isóceles')
else:
    print('escaleno')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break