from random import randint
sep1 = '-=' * 28
sep2 = '-' * 56
pontos = 0
print(sep1)
titulo = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'{titulo:^56}')
print(sep1)
while True:
    pc = randint(1, 10)
    jogada = int(input('Digite um valor: '))
    pi = 'X'
    while pi != 'P' and pi != 'I':
        pi = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0].replace('Í', 'I')
    total = jogada + pc
    print(sep2)
    print(f'Você jogou {jogada} e o computador {pc}. Total de {total}.', end=' ')
    if total % 2 == 0:
        print('Deu PAR.')
        rodada = 'P'
    else:
        print('Deu ÍMPAR.')
        rodada = 'I'
    print(sep2)
    if pi == rodada:
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
        print(sep1)
        pontos += 1
    else:
        print('Você PERDEU!')
        break
print(sep1)
print('GAME OVER!', end=' ')
if pontos == 0:
    print('Você não ganhou nenhuma vez.\n')
elif pontos == 1:
    print('Você ganhou somente 1 vez.\n')
else:
    print(f'Você ganhou {pontos} vezes.\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio68', 'r')
    print(f.read())