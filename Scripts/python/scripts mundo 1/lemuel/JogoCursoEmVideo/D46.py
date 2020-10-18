from time import sleep
print('Contagem regressiva para estourar os fogos de artifício:')
for c in range(10, 0 - 1, -1):
    sleep(1)
    if c != 0:
        print('{}...\n'.format(c))
    else:
        print('BOOOM!\n')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D46', 'r')
    print(f.read())
