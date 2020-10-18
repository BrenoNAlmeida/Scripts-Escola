v=float(input('qual foi a sua velocidade ?'))
m= (v-80)*7
if v > 80:
    print('você fou multado , sua multa é de R${}'.format(m))
else:
    print('você não foi multado, parabéns')