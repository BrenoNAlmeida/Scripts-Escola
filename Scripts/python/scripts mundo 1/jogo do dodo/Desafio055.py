maior_peso = 0
menor_peso = 1000000
for p in range(1,6):
    peso = float(input('qual o peso {}° pessoa ?  '.format(p)))
    if peso > maior_peso :
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('o maior peso é {}Kg'.format(maior_peso))
print('o menor peso é {}Kg'.format(menor_peso))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break