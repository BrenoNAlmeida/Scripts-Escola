nome = input('Digite seu nome completo: ').strip().split()
qtd = len(nome)
print('Seu primeiro nome é {} e seu último nome é {}!'.format(nome[0], nome[qtd-1]), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D27', 'r')
    print(f.read())