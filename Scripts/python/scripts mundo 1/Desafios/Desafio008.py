n=float(input('\033[4;31mdigite a quantidade de metros = \033[m'))
c=n*100
m=n*1000
cores={'azul':'\033[34m',
       'vermelho':'\033[31m',
       'apagar':'\033[m'}
print('{}O valor em centimetros é : {}{}{}{}'.format(cores['azul'],cores['apagar'],cores['vermelho'],c,cores['apagar']))
print('{}O valor em milímetros é : {}{}{}{}'.format(cores['azul'],cores['apagar'],cores['vermelho'],m,cores['apagar']))