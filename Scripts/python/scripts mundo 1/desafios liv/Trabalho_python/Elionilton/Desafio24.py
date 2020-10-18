cidade = input('Digite o nome da cidade: ')
cl = cidade.upper().strip().split()
res = cl[0] == 'SANTO'
print('\nA cidade começa ou não com a palavra "Santo"? True significa Sim e False significa Não.')
print('Resposta: {}'.format(res), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio24', 'r')
    print(f.read())