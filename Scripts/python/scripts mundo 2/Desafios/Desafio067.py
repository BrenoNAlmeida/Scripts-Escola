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