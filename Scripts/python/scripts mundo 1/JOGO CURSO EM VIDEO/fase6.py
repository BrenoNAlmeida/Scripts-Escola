print('''\033[34mOS EXERCICIOS DESSA FASE SÃO :
\033[32m [3] - Somando dois numeros
[4] - Analisando uma variavel\033[m''')
opção3 = int(input('QUAL EXERCICIO VOCÊ QUER EXECUTAR ? '))
if opção3 == 3:
    import exercicio03
elif opção3 == 4:
    import exercicio04
