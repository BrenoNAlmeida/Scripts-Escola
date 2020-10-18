ter = int(input('digite o primeiro termo da PA: '))
raz = int(input('digite a razão da PA: '))
pa = 1
termo = ter
total = 0
more = 10
while more != 0:
    total = total + more
    while pa <= total:
         print('{} -> '.format(termo), end='')
         termo += raz
         pa += 1
    print('PAUSE')
    more = int(input('qunatos termos a mais você quer, ?'))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break