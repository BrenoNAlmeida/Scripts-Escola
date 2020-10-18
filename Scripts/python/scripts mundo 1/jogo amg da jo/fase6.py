print('''\033[34mOs desafios dessa fase sao esses {} :
\033[32m 3 = Somando dois numeros
4 = Analisando uma variavel\033[m''')
escolha3 = int(input('qual desafio você deseja ?'))
if escolha3 == 3:
    import exercicio003
elif escolha3 == 4:
    import exercicio004
