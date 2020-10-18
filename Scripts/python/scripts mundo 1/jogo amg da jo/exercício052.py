#exercício052
tot = 0
n = int(input('digite um numero inteiro : '))
for c in range (1, n +1):
    if n % c == 0:
        print('\033[33m')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mo numero {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('primo')
else:
    print('n é primo')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break