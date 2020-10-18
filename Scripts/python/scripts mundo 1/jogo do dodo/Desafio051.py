ooh_god = int(input('O primeiro termo = '))
jesus_socorro = int(input('Razão = '))
grr = (ooh_god + (10) * jesus_socorro)
for socorro in range(ooh_god,grr,jesus_socorro):
    print('{}'.format(socorro), end= '-> ')
print('FIM')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break