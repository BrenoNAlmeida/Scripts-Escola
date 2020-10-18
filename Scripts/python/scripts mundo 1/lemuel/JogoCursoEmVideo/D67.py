sep = '-' * 20
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print(sep)
    for n in range(1, 10 + 1):
        print(f'{tabuada} x {n:2} = {tabuada * n}')
    print(sep)
print(sep)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!\n')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D67', 'r')
    print(f.read())