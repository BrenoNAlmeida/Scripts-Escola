n1 = int(input('digite aqui um número: '))
n2 = int(input('digite aqui outro número'))
es = ''
soma = n1 + n2
mult = (n1) * (n2)
maiornum = 0
while es != 5 :
    print('''Escolhas
[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior \n[ 4 ] Novos números\n[ 5 ] Sair do programa''')
    es = int(input('qual a sua escolha? '))
    if es == 1:
        print('a soma de {} com {} é {}'.format(n1, n2, soma))
    if es == 2:
        print('o produto entre {} e {} é {}'.format(n1, n2, mult))
    if es == 3:
        if n1 > maiornum:
            maiornum = n1
        if n2 > maiornum:
            maiornum = n2
        print('o maior número é {}'.format(maiornum))
    if es == 4:
        n1 = int(input('digite aqui outro número: '))
        n2 = int(input('digite aqui outro número: '))
print('fim')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break