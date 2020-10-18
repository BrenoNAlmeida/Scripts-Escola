#exercício071
eg = '='
print('{}\n         CAIXA ELETRÔNICO\n{}'.format(eg*35, eg*35))
valor  = int(input('quanto você quer sacar R$'))
tot = valor
cin = 50
c = 0
d = 0
dd = 0
u = 0
while True:
    while tot >= cin:
        tot -= cin
        c += 1
    else:
        print(f'{c} cédulas de 50')
        while tot >= 20:
            tot -= 20
            d += 1
        if d != 0:
            print(f'{d} cédulas de 20')
        while tot >= 10:
            tot -= 10
            dd += 1
        if dd != 0:
            print(f'{dd} cédulas de 10')
        while tot >= 1:
            tot -= 1
            u += 1
        if u != 0:
            print(f'{u} cédulas de 1')
        if tot == 0:
            break

print('Obrigador por utilizar nossos programas ')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break