r=float(input('\033[4;31mquantos reais você tem ?\033[32m R$\033[m'))
d=r/3.27
cores={'vermelho':'\033[31m',
       'apagar':'\033[m'}
print('com R${}{}{} , você pode trocar por US${}{:.2f}{}'.format(cores['vermelho'],r,cores['apagar'],cores['vermelho'],d,cores['apagar']))