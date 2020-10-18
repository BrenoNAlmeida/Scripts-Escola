nome = input('Qual é o seu nome? ')
print('Olá', nome, '! Prazer em te conhecer!\n')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D1', 'r')
    print(f.read())
