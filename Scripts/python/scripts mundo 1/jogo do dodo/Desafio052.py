obg_adorilson = int(input('digite um numero inteiro = '))
quant = 0
for tio_dodo in range(1, obg_adorilson + 1):
    if obg_adorilson % tio_dodo == 0:
        quant = quant + 1
if quant > 2:
    print('o numero {} não é primo'.format(obg_adorilson))
else:
    print('o numero {} é primo'.format(obg_adorilson))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break