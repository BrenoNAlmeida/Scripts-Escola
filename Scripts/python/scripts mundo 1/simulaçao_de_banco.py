from time import sleep
ultimo = 10
fila = list(range (1 ,ultimo+1))
while True:
    print('\n Existem %r clientes na fila' % len(fila))
    print('''fila atual = {} 
    Digite F para adicionar um cliente ao fim da fila,
    ou A para para realizar o atendimento . S para sair :'''.format(fila))
    op = str(input('digite a operação desejada [ F, A, S] :')).upper()
    if op == 'A':
        if (len(fila))>0:
            atendido= fila.pop(0)
            print('cliente %r atendidio' %atendido)
        else:
            print(' a fla esta fazia .')
    elif op == 'F':
        ultimo += 1
        fila.append(ultimo)
        print('cliente adicionado com sucesso')
    elif op == 'S':
        break
    else:
        print('operaçao invalida, o programa será executado em seguida')
        for c in range(0,3):
            print(c)
            sleep(1)