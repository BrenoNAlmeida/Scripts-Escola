#adição de elementos
'''l =[]
r ='S'
while r == 'S':
    a = str(input(' digite um nome '))
    l.append(a)
    op = str(input('você deseja adicionar outro nome [S/N]?')).upper()[0]
    if op == 'N':
        print('os nomes adicionados foram {}'.format(l))
        break'''
'''#junção de elementos
L1 = ['breno', 'adna', 'fabio']
L2 = ['diogo', 'juciele','vitor']
L1.extend(L2)
print(L1)

# remoção de elementos
apagar = int(input('qual vc deseja remover ?'))
del L1[apagar]
print(L1)'''
'''from time import sleep
p = 0
fila = ['breno', 'adna', 'fabio']
while fila != []:
    print(fila.pop(0))
    sleep (0.2)
'''
#remoção por elemento
'''
L = [1,2,3,4,5,6,7,8,9,10]
print(L)
r = int(input('qual elemento voçê deseja remover ?'))
L.remove(r)
print(L)
es = str(input('voçê deseja remove mais algum elemento, [SIM/NAO]'))
while es != 'SIM' or es != 'NAO':
    if es == 'SIM':
        import aula_de_lista
    else:
        print('adeus')'''
def f(x):
    y = 10 + x
    return y
x = int(input())
print(f(x))