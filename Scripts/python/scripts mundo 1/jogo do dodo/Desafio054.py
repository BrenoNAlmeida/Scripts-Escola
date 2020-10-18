from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(0 ,7):
    idade = int(input('qual a pessoa nasceu ? '))
    calc = data - idade
    if calc > 17 :
        maior = maior + 1
    else:
        menor = menor + 1
print(' o numero de pessoas maior de idade é {} '.format(maior))
print(' o numero de pessoa menor de idade é  {}'.format(menor))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break