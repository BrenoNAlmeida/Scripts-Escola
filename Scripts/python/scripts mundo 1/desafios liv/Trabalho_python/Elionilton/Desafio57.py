sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('Valor inválido! Digite M para sexo MASCULINO ou F para sexo FEMININO.')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Você do sexo MASCULINO!\n')
elif sexo == 'F':
    print('Você é do sexo FEMININO!\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio57', 'r')
    print(f.read())