import datetime
pelo_amor_de_samuel = datetime.date.today().year
chegaaa = int(input('Qual a data do seu nascimento ?'))
meu_deus = pelo_amor_de_samuel - chegaaa
sou_burro = 18 - meu_deus
if sou_burro > 0 :
    print('você ainda vai se alistar , falta {} anos'.format(sou_burro))
elif sou_burro < 0:
    print('ja passou do tempo de você se alistar, você esta atrasado {} anos'.format((sou_burro)*-1))
else:
    print('esta na hora de você se alistar , vá ainda esse ano ')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break