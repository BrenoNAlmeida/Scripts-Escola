from time import sleep
queria_dormir = float(input('qual o valor do produto ?'))
ai_deus = (120 * queria_dormir )// 100
print('formas de pagamento ?')
print('digite 1 para à vista no dinheiro \ndigite 2 para à vista no cheque ')
print('digite 3 para cartão')
adeus_feriado = input('Qual forma de pagamento você deseja ?')
if adeus_feriado == '1' :
    print('o valor do produto vai ficar {}'.format(queria_dormir -((queria_dormir *10))//100))
elif adeus_feriado == '2' :
    print('o valor do produto vai ficar {}'.format(queria_dormir -((queria_dormir *10))//100))
elif adeus_feriado == '3':
    print('vócê vai pagar :\n Digite 1 para à vista \n digite 2 para dividir em 2 vezes')
    print('digite 3 para dividir em 3 vezes ou mais')
    socorro =int( input('qual das opções você deseja ? '))
    print('Calculando ...')
    sleep(3)
    if socorro == 1 :
        print('o valor do produto vai ficar {}'.format(queria_dormir -((queria_dormir *10))//100))
    elif socorro == 2:
        print('o valor do produto vai ficar R${} mensal '.format(queria_dormir //2))
    elif socorro == 3:
        print('o valor do produto vai ficar R${} mensal'.format((queria_dormir + ai_deus )))
    else:
        print('\033[31m ERRO , EXECUTE NOVAMENTE\033[m')
else:
    print('\033[31m ERRO, EXECUTE NOVAMENTE ')
print('Obrigado pela compra , volte sempre !')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break