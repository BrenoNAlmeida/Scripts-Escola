nome = input('Digite seu nome completo: ')
nl = nome.upper().strip()
res = 'SILVA' in nl
print('Você possui "Silva" no nome? True significa Sim e False significa Não.\nResposta: {}'.format(res), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio25', 'r')
    print(f.read())