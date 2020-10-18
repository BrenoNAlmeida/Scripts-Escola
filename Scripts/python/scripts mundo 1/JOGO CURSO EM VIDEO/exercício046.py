from time import sleep
for cont in range (10,-1, -1):
    print(cont)
    sleep(0.8)
print('BUM! BUM! BUM! POOOOOOOW! ')
print('Feliz ano NOVO! ')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
