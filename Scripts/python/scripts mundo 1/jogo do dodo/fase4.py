print('\033[33;1mOs desafios dessa fase são esses :'
          '\n 1 = Deixando tudo pronto'
          '\n 2 = Respondendo ao usuario\033[m')
desafio = int(input('qual desafio você deseja ? '))
if desafio == 1:
    import Desafio001
if desafio == 2:
    import Desafio002
