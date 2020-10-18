print('\033[31m calcule a sua media semestral\033[m')
jesus = float(input('Digite sua primeira nota '))
socorro = float(input('Digite sua segunda nota\n'))
coitado_de_mim = (jesus + socorro)/2
print('A sua nota é {}\n'.format(coitado_de_mim))
if coitado_de_mim < 50 :
    print('Reprovado , estude mais')
elif coitado_de_mim > 59 :
    print('parabéns , você foi aprovado')
else:
    print('você esta em Recuperação , boa sorte')
