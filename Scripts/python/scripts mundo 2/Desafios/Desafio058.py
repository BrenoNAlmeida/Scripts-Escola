from random import randint
cont = 1
num = randint(0, 10)
adi = int(input('qual o numero que eu pensei ?  '))
if adi == num:
    print('UAU ! Você acertou de primeira.\nEu pensei em {} '.format(num))
else:
    while adi != num:
        if num > adi:
            print('ops, você errou, o numero que eu pensei é maior. Tente novamente ')
            adi = int(input('qual o numero que eu pensei ?'))
            cont+= 1
        else:
            print('ops, você errou, o numero que eu pensei é menor. Tente novamente ')
            adi = int(input('qual o numero que eu pensei ?'))
            cont+= 1
    print('você acertou, eu pensei em {} também\nvocê precisou de {} tentativas'.format(num, cont))