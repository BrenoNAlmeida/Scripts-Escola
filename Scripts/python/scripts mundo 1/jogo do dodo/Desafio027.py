nome=str(input('digite seu nome completo =')).capitalize()
trans=nome.split()
print('seu primeiro nome é {}'.format(trans[0]))
print('e seu ultimo nome é {}'.format(trans[len(trans)-1] ))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break