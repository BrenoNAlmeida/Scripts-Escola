s=float(input('quanto é o seu salario ?'))
a1=(s*10)/100
a2=(s*15)/100
if s >= 1250.00:
    print ('seu almento sera de {}'.format(a1))
else:
    print('seu almento sera de {}'.format(a2))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
