soma = 0
cont = 0
for c in range(1, 9):
    num = int(input('Digite o {} o valor: '.format(c)))
    if num % 2 == 0:
         soma += num
         cont += 1
print('Os numeros escolhidos {} numeros PARES e a soma foi  {}'.format(cont,soma))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
