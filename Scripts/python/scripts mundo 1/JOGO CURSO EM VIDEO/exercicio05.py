n = int(input('Digite um numero: '))
print('observando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,(n-1), (n+1),))

opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
