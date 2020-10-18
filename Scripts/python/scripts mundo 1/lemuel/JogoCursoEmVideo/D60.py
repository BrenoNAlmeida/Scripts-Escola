numero = int(input('Digite um número para descobrir seu fatorial: '))
copia = numero
resultado = numero
add = ''

while copia > 0:
    if copia != numero:
        resultado *= copia
    add += str(copia)
    if copia != 1:
        add += ' x '
    copia -= 1

print('{}! = {} = {}\n'.format(numero, add, resultado))

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D60', 'r')
    print(f.read())

