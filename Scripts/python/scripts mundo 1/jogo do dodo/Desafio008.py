n=float(input('\033[4;31mdigite a quantidade de metros = \033[m'))
c=n*100
m=n*1000
cores={'azul':'\033[34m',
       'vermelho':'\033[31m',
       'apagar':'\033[m'}
print('{}O valor em centimetros é : {}{}{}{}'.format(cores['azul'],cores['apagar'],cores['vermelho'],c,cores['apagar']))
print('{}O valor em milímetros é : {}{}{}{}'.format(cores['azul'],cores['apagar'],cores['vermelho'],m,cores['apagar']))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break