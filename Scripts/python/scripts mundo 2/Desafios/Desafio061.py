print('ache os termos de uma PA ')
p =int(input('qual o primeiro termo ? '))
raz = int(input('qual a Razão'))
termo = p
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('Fim')