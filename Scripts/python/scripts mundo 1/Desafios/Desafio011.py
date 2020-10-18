h=float(input('\033[4;35mqual a altura da parede em metros ? '))
print('\033[32m=='*13)
l=float(input('\033[35mqual a largura da parede em metros ? \033[m'))
print('\033[32m=='*13)
a=h*l
qt=a/2
cores={'roxo':'\033[35m',
       'apagar':'\033[m',
       'vermelho':'\033[31m'}
print('{}A área da sua parede é de : {} m²{} '.format(cores['roxo'],cores['vermelho'],a,cores['apagar']))
print('{}A quantidade de tinta necessaria será de {}{} Litros'.format(cores['roxo'],cores['vermelho'],qt))