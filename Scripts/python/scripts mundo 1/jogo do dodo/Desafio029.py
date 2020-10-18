v=float(input('qual foi a sua velocidade ?'))
m= (v-80)*7
if v > 80:
    print('você fou multado , sua multa é de R${}'.format(m))
else:
    print('você não foi multado, parabéns')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break