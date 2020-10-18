d=int(input('\033[35mquantos dias o carro foi alugado ?'))
k=float(input('quantos quilometros o carro rodou ?\033[m'))
print('\033[32m=='*23)
cores={'limpa':'\033[m',
       'roxo':'\033[35m',
       'vermelho':'\033[31m'}
p=(60*d)+(0.15*k)
print('{}O total a pagar pelo aluguel será de {}R${}'.format(cores['roxo'],cores['vermelho'],p))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break