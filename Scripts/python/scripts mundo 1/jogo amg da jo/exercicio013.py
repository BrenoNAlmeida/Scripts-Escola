s=float(input('Quanto é o seu salario ? R$'))
a=(s*35)/100
ns=s+a
print('o seu aumento sera de R$ {:.5}'.format(a))
print('o seu novo salario é R${:.5}'.format(ns))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
