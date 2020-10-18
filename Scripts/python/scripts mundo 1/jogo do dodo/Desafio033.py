v1=float(input('primeiro valor ='))
v2=float(input('segundo valor ='))
v3=float(input('terceiro valor='))
me=v1
if v2 < v1 and v2 < v3:
    me = v2
if v3 < v1 and v3 < v2:
    me = v3
ma=v1
if v2 > v1 and v2 > v3:
    ma=v2
if v3 > v1 and v3 > v2:
    ma = v3
print('o menor valor entre {} , {} e {} é  {}'.format(v1,v2,v3,me))
print('o maior valor entre {} , {} e {} é {}'.format(v1,v2,v3,ma ))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break