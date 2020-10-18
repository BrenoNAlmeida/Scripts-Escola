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
