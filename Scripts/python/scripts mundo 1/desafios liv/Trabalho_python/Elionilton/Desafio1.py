nome = input('Qual é o seu nome? ')
print('Olá', nome, '! Prazer em te conhecer!\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio1', 'r')
    print(f.read())