#exercício067
desg = '-'
print(f'{desg *20}\n     TABUADA\n{desg *20}')
n = 0
while n >= 0:
    n = int(input('Digite um número para vê sua tabuada \n\033[31m(Para parar, digite número negativo rs)\033[m '))
    if n < 0:
        break
    else:
        print(f'{desg*20}\n  TABUADA DE {n}\n{desg*20}')
        for c in range(1,11):
            print(f'{n} * {c} = {n*c}')
        print(f'{desg*20}')
print('\033[34mObrigado por usar nossos serviços, a Pote 2 agradece.\033[m')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break