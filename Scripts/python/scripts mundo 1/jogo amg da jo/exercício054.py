#exercício054
v = 0
s = 0
for maior in range (1, 8):
    id = int(input('\033[;39mEm que ano vc nasceu? \033[m'))
    if 2017- id > 18 or 2017 - id == 18:
        s += 1
        print('\033[;34m você já é de maior, bu!\033[m')
    else:
        v +=1
        print('\033[;31m você ainda é de menor.\033[m')
print('-'*50)
print('{} pessoas possuem a maioridade penal atingida.'.format(s))
print('E {} pessoas não atigiram a maioridade penal.'.format(v))
print('--'*25)
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break