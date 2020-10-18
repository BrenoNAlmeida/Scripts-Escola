pa_pa_pa= int(input(' de que numero você deseja a tabuada ?'))
for oloko in range(0,11):
    ja_ja = (oloko * pa_pa_pa )
    print( '{} X {} = {}'.format(pa_pa_pa,oloko,ja_ja))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break