
from time import sleep
pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:

    print('''\nO que deseja fazer?\n
[ 1 ] SOMAR VALORES
[ 2 ] MULTIPLICAR VALORES
[ 3 ] DESCOBRIR O VALOR MAIOR
[ 4 ] DIGITAR NOVOS VALORES
[ 5 ] SAIR DO PROGRAMA\n''')

    escolha = int(input('Escolha a sua opção (1 a 5): '))

    while escolha < 1 or escolha > 5:
        print('\nOpção inválida!\n')
        escolha = int(input('Escolha a sua opção (1 a 5): '))

    if escolha == 1:
        print('\n{} + {} = {}'.format(pv, sv, pv + sv))
        sleep(3)
    elif escolha == 2:
        print('\n{} x {} = {}'.format(pv, sv, pv * sv))
        sleep(3)
    elif escolha == 3:
        if pv > sv:
            print('\nO primeiro valor ({}) é maior do que o segundo ({}).'.format(pv, sv))
        elif sv > pv:
            print('\nO segundo valor ({}) é maior do que o primeiro ({}).'.format(sv, pv))
        else:
            print('\nO primeiro ({}) e o segundo ({}) são valores iguais.'.format(pv, sv))
        sleep(3)
    elif escolha == 4:
        print('')
        pv = int(input('Digite o primeiro valor: '))
        sv = int(input('Digite o segundo valor: '))

print('Programa finalizado!\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio59', 'r')
    print(f.read())