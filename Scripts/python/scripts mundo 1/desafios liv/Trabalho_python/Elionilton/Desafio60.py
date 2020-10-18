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

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio60', 'r')
    print(f.read())

