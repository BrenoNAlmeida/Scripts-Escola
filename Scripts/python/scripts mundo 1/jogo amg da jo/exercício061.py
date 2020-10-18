#exercício061#adorobb#diogocode
ter = int(input('digite o primeiro termo da PA: '))
raz = int(input('digite a razão da PA: '))
pa = 1
termo = ter
while pa <= 10:
     print('{} -> '.format(termo), end='')
     termo = termo + raz
     pa += 1
print('\nfim')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break