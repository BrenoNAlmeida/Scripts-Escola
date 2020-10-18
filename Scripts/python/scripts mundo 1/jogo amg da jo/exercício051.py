#exercício051
ter = int(input('digite o primeiro termo da PA: '))
raz = int(input('digite a razão da PA: '))
for pa in range (1,11):
    v = (ter + ((pa - 1)*raz))
    print(v)
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break