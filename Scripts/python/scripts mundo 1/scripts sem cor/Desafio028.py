import random
pc=random.randint(0,5)
print('==='*20)
print('tente adivinhar o numero  de 0 á 5  em que eu pensei ,!')
print('==='*20)
player=int(input('Qual numero você acha que eu pensei ?'))
if player == pc:
    print('parabens , eu realmente pensei em {} , você acertou !'.format(player))
else:
    print('HA HA , eu pensei em {} ,eu ganhei , tente novamente !'.format(pc))