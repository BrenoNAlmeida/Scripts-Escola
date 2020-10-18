print('\033[1;31m comparando valores \033[m')
ja_chega = float(input('digite um valor'))
desisto = float(input('digite um valor '))
if ja_chega > desisto:
    print('o primeiro valor é maior !!')
elif desisto > ja_chega:
    print('o segundo valor é maior !!')
else:
    print('os dois valores são iguais')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break