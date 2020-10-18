s=float(input('\033[1mquanto é o seu salario ?\033[m'))
a1=(s*10)/100
a2=(s*15)/100
if s >= 1250.00:
    print ('\033[1;34mseu almento sera de {}\033[m'.format(a1))
else:
    print('\033[1;31mseu almento sera de {}\033[m'.format(a2))

