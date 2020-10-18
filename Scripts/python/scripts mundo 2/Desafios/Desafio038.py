print('\033[1;31m comparando valores \033[m')
ja_chega = float(input('digite um valor'))
desisto = float(input('digite um valor '))
if ja_chega > desisto:
    print('o primeiro valor é maior !!')
elif desisto > ja_chega:
    print('o segundo valor é maior !!')
else:
    print('os dois valores são iguais')