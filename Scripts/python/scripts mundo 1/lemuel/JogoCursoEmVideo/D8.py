n = int(input('Digite o valor em metros: '))
cm = n * 100
mm = n * 1000
print('{} metro(s) equivale(m) a {} centímetros ou a {} milímetros.'.format(n, cm, mm), "\n")

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D8', 'r')
    print(f.read())
