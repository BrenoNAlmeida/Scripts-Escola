from time import sleep
print('\033[31m contagem regressiva dos fogos vai começar\033[m')
sleep(3)
for c in range (10,0,-1):
    print(c)
    sleep(1)
print('\033[31m CABUUUUUUMMMMM')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break