not1 = float(input('digite sua nota '))
not2 = float(input('digite sua nota '))
med = ((not1+not2)/2)
if med < 5:
    print('\033[1;33mREPROVADO!\033[m')
elif med > 5 and med < 6.9:
    print('\033[1;35mRECUPERÇÃO\033[m')
elif med > 7:
    print('APROVADOOOO')
print('média: {}'.format(med))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break