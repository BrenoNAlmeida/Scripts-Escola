p=float(input('\033[32mqual o preço do produto ? R$\033[m'))
d=(p*5)/100
v=p-d
print('\033[34mO desconto em 5 porcento do produto será de \033[31mR${}\033[34m'.format(d))
print('O valor do produto com 5 porcento de desconto é de \033[31mR${}'.format(v))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break