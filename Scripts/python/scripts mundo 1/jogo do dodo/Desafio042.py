r1 = float(input('\033[1;34mprimeiro segmento = '))
r2 = float(input('\033[1;34;msegundo segmento = '))
r3 = float(input('\033[1;34;mterceiro segmento = '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('messes segmentos podem forma um triangulo')
    if r1 == r2  == r3:
     print('um triangulo é Equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
     print('um triangulo é Isósceles ')
    else:
     print('um triangulo é Éscaleno')
else:
    print('esses segmentos NÃO podem formar um triangulo')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break