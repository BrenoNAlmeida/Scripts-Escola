núm = int(input('Digte o numero: '))
tot = 0
for c in range(1, núm + 1):
  if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
  else:
      print('\033[31m', end='')
  print('{} '.format(c), end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(núm, tot))
if tot == 2:
    print('PORTANTO ELE É PRIMO! ')
else:
    print('PORTANTO ELE NÃO É PRIMO! ')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
