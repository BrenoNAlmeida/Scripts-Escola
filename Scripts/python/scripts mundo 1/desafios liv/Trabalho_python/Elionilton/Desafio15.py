km = float(input('Qual foi a quantidade de quilômetros percorridos pelo carro alugado? '))
d = int(input('Por quantos dias ele foi alugado? '))
t = (d * 60) + (km * 0.15)
print('O carro alugado por {} dias percorreu {:.2f} quilômetros, e com isso será preciso pagar R$ {:.2f}!'.format(d, km, t), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio15', 'r')
    print(f.read())
