#exercício055
maiorpeso = 0
menorpeso = 1000000
for p in range (1,6):
    pe = int(input('peso da {}ª pessoa: '.format(p)))
    if pe > maiorpeso:
        maiorpeso = pe
    if pe < menorpeso:
        menorpeso = pe
print('o maior peso é {} kg.'.format(maiorpeso))
print('o menor peso é {} kg.'.format(menorpeso))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break