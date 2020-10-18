print ('diga me a sua data de nascimento ?')

dia=input('Dia =')
mes=input('Mes =')
ano=input('Ano =')
escolha4 = ''
print ('você nasceu no dia',dia,'de',mes,'de',ano,'.Correto ?')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break