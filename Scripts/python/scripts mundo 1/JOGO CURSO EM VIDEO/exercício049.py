num = int(input('Digite um numero para acessar  tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num,c, num*c))

print('ACABOU AIII')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
