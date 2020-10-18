to_desistindo = 0
for vdc in range (0,6):
    opa_bb = int (input('digite um numero inteiro'))
    if opa_bb % 2 == 0:
        to_desistindo = to_desistindo + opa_bb
    else:
        to_desistindo = to_desistindo
print('a soma dos numeros é = {}'.format(to_desistindo))
print('os numeros impares foram desconsiderados ')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break