porque_to_vendo_isso = float(input('qual o preço da casa que você deseja comprar ? R$'))
me_matem = float(input('quanto é o seu salario ? R$'))
eu_tenho_problemas = int(input('em quantos anos você deseja pagar'))
socorro = porque_to_vendo_isso // (eu_tenho_problemas*12)
me_ajudem = (30*me_matem)//100
if socorro > me_ajudem:
    print(' Desculpe ,mas voce nao pode comprar a casa ')
else:
    print('Parabeéns ,você poderá comprar a casa , a mensalidade será de R${}'.format(socorro))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break