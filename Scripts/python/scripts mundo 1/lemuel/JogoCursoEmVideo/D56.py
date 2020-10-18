totalidade = 0
maisvelho = 0
nomemaisvelho = ''
mulheresjovens = 0
for c in range(1, 4 + 1):
    msg1 = 'Digite o nome da pessoa Nº {} (ex: Maria): '.format(c)
    msg2 = 'Digite a idade da pessoa Nº {} (ex: 25): '.format(c)
    msg3 = 'Digite o sexo da pessoa Nº {} (H para homem ou M para mulher): '.format(c)
    nome = str(input(msg1)).strip()
    idade = int(input(msg2))
    sexo = str(input(msg3)).strip().lower()
    print()
    totalidade += idade
    if idade > maisvelho and sexo == 'h':
        maisvelho = idade
        nomemaisvelho = nome
    if idade < 20 and sexo == 'm':
        mulheresjovens += 1

media = int(totalidade / 4)
print('A média de idade do grupo é {} anos.'.format(media))

if nomemaisvelho == '':
    print('Não tem nenhum homem no grupo.\n')
else:
    print('O homem mais velho do grupo tem {} anos e se chama {}.\n'.format(maisvelho, nomemaisvelho))

if mulheresjovens == 0:
    print('Não tem nenhuma mulher com menos de 20 anos no grupo.\n')
elif mulheresjovens == 1:
    print('Tem somente uma mulher com menos de 20 anos no grupo.\n')
else:
    print('Tem {} mulheres com menos de 20 anos no grupo.\n'.format(mulheresjovens))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D56', 'r')
    print(f.read())
