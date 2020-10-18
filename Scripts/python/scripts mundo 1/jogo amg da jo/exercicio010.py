r=float(input('quantos reais você tem ? R$'))
d=r/3.27
print('com R${} , você pode trocar por US${:.2f}'.format(r,d))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break