r1 = float(input('primeiro segmento = '))
r2 = float(input('segundo segmento = '))
r3 = float(input('terceiro segmento = '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('messes segmentos podem forma um triangulo')
else:
    print('esses segmentos NÃO podem formar um triangulo')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break