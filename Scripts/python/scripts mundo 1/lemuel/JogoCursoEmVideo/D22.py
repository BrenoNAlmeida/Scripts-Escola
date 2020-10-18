nome = input('Digite seu nome completo: ')
nome_sem_espacos = len(nome) - nome.count(' ')
primeiro_nome = len(nome.split()[0])
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Quantidade total de letras (sem contar os espaços): {}'.format(nome_sem_espacos))
print('Quantidade de letras do primeiro nome: {}'.format(primeiro_nome), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D22', 'r')
    print(f.read())