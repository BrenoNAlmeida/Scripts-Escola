r=float(input('\033[4;31mquantos reais você tem ?\033[32m R$\033[m'))
d=r/3.27
cores={'vermelho':'\033[31m',
       'apagar':'\033[m'}
print('com R${}{}{} , você pode trocar por US${}{:.2f}{}'.format(cores['vermelho'],r,cores['apagar'],cores['vermelho'],d,cores['apagar']))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break