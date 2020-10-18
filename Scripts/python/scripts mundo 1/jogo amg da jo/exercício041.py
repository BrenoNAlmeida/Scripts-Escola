print('\033[;36m=-\033[m'*10)
print('\033[1mCATEGORIA NA NATAÇÃO\033[m')
print('\033[;36m=-\033[m'*10)
yer = int(input('em que ano você nasceu? '))
idd = 2017-yer
if idd<9 or idd == 9:
    print('MIRIM')
elif idd<14 and idd>9 or idd == 14:
    print('INFANTIL')
elif idd>14 and idd<19 or idd == 14 or idd == 19:
    print('JUNIOR')
elif idd > 19 and idd < 20 or idd == 20:
    print('SÊNIO')
else:
    print('MASTER')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break