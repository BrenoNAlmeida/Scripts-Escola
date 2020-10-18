num = float(input('digite um valor '))
num2 = float(input('digite outro valor  '))
op = ''
while op != 5:
    print('[1] para somar\n[2] para multiplicar\n[3] para maior valor'
          '\n[4] para novos numeros\n[5] para sair do programa')
    op = int(input('qual opção você deseja ?'))
    if op == 1 :
        print('a somar dos numeros é {}'.format(num + num2))
    elif op == 2:
        print('{} X {} = {}'.format(num, num2, num * num2))
    elif op == 3:
        if num > num2:
            print(' o maior numero é {}'.format(num))
        else:
            print(' o maior numero é {}'.format(num2))
    elif op == 4:
        num = float(input('digite um valor '))
        num2 = float(input('digite outro valor  '))
print('obrigado por usar nossos serviços')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break