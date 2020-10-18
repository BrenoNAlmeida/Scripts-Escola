d=int(input('\033[35mquantos dias o carro foi alugado ?'))
k=float(input('quantos quilometros o carro rodou ?\033[m'))
print('\033[32m=='*23)
cores={'limpa':'\033[m',
       'roxo':'\033[35m',
       'vermelho':'\033[31m'}
p=(60*d)+(0.15*k)
print('{}O total a pagar pelo aluguel será de {}R${}'.format(cores['roxo'],cores['vermelho'],p))