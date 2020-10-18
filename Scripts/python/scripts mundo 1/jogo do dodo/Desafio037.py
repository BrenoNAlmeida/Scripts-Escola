print('\033[36m Converta bases numericas\033[m')
socorro = int(input('Digite um numero inteiro = '))
print('Para qual base numerica você deseja converter ? ')
print(' digite 1 para BINARÍO\n digite 2 para OCTADECIMAL\n digite 3 para HEXADECIMAL ')
adorilsonzinho = int(input('qual sua escolha ?'))
if adorilsonzinho == 1 :
    print('o numero {} em binarío é {}'.format(socorro, bin(socorro)))
elif adorilsonzinho == 2 :
    print('o numero {} em octadecimal é {}'.format(socorro,oct(socorro)))
elif adorilsonzinho == 3 :
    print('o numero {} em hexadecimal é {}'.format(socorro , hex(socorro)))
else:
    print('ERRO , execute novamente')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break