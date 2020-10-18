nome=input('qual o seu nome ?')
print ('diga me a sua data de nascimento ?')
dia=input('Dia =')
mes=input('Mes =')
ano=input('Ano =')
print ('ola',nome,'você nasceu no dia',dia,'de',mes,'de',ano,'.Correto ?')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break