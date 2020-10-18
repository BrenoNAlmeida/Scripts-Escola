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
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break