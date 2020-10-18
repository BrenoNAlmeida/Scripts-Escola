num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
{ 1 } converter para BINARIO 
{ 2 } converter para OCTAL
{ 3 } converter para HEXADECIMAL''')
opcao = int(input('sua opçao: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXDECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida. Tente novamnte.')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
