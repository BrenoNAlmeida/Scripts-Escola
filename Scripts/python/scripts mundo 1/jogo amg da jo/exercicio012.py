p=float(input('qual o preço do produto ? R$'))
d=(p*5)/100
v=p-d
print('O desconto em 5 porcento do produto será de R${}'.format(d))
print('O valor do produto com 5 porcento de desconto é de R${}'.format(v))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break