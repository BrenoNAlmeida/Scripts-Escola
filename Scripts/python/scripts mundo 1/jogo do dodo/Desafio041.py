import datetime
deus = int(input('qual a data de nascimento do atleta ?'))
god = datetime.date.today().year
me_salvem = 2017 - deus
if me_salvem < 10 :
    print('a categoria do atleta é MIRIM')
elif me_salvem < 15 :
    print('a categoria do atleta é INFANTIL ')
elif me_salvem < 20:
    print('a categoria do atleta é JUNIOR')
elif me_salvem < 21:
    print('a categoria do atleta é SENIOR')
else:
    print('a categoria do atleta é MASTER')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break