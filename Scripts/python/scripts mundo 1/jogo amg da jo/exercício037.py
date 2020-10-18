num = int(input('digite um número inteiro '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] Converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário é igaul a {}'.format(num, bin(num)[2:]))
elif opção ==2:
    print('{} convertido para octal é igaul a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break