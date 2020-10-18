print('empréstimo bancário')
val = float(input('qual o valor da casa? R$'))
sal = float(input('qual o seu salário? R$'))
time = float(input('em quantos anos x senhorx irá pagar? R$'))
prestaçao = ((val)/(time*12))
print('a prestação será de: R${:.2f}'.format(prestaçao))
if prestaçao > ((30*sal)/(100)):
    print('empréstimo negado')
else:
    print('empréstimo concedido')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break