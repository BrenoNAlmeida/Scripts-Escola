from random import choice
opcoes = ['pedra', 'papel', 'tesoura']
adv = choice(opcoes)
print('Digite qual você quer jogar!')
jogador = str(input('PEDRA, PAPEL ou TESOURA? ')).lower().strip()
if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
    print('Você jogou {} e eu joguei {}.'.format(jogador.upper(), adv.upper()))
    if adv == jogador:
        print('Nós empatamos!\n')
    elif adv == 'pedra' and jogador == 'papel':
        print('Você ganhou!\n')
    elif adv == 'pedra' and jogador == 'tesoura':
        print('Eu ganhei!\n')
    elif adv == 'papel' and jogador == 'pedra':
        print('Eu ganhei!\n')
    elif adv == 'papel' and jogador == 'tesoura':
        print('Você ganhou!\n')
    elif adv == 'tesoura' and jogador == 'pedra':
        print('Você ganhou!\n')
    elif adv == 'tesoura' and jogador == 'papel':
        print('Eu ganhei!\n')
    else:
        print('Erro!\n')
else:
    print('Jogada inválida! Digite PEDRA, PAPEL ou TESOURA!\n')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D45', 'r')
    print(f.read())
