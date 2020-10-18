x= int(input('bla bla bla = '))
e_primo = True
for n in range (2 , x):
    if x % n == 0:
        e_primo = False
        break
if e_primo:
    print('o numero é primo ')
else:
    print('nao é primo')
