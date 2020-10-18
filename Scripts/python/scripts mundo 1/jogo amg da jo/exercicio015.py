d=int(input('quantos dias o carro foi alugado ?'))
k=float(input('quantos quilometros o carro rodou ?'))
p=(60*d)+(0.15*k)
print(f'O total a pagar pelo aluguel será de R${p}')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break