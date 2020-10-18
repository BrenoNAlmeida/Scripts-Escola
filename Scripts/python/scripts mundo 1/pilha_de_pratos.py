prato = 5
pilha = list(range(1,prato + 1))
while True:
    print(' existem %d pratos na pilha '%len(pilha))
    print('''pilha atual  = {}
    digite E para adicionar um novo prato a pilha,
    ou D para lavar um prato. S para sair''')
    op = str(input('qual operaçao você deseja :'.format(pilha))).upper()
    if op == 'E':
        prato+= 1
        pilha.append(prato)
    if op == 'D':
        if (len(pilha))>0:
            lavado = pilha.pop(-1)
            print('prato {} lavados'.format(lavado))
    elif op == 'S':
        print('obrigado por ultlzar nossos serviços')
        break