n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print ('0 dobro de {} vale {}.'.format(n,d))
print ('0 triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
