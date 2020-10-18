print('== CASA DA JU ==')
pessoas_que_vao = []
op = 'nao'
while True:
    pessoa = str(input(' quem vai pra casa da ju ?'))
    pessoas_que_vao.append(pessoa)
    op = str(input('mais alguma pessoa vai ?'))
    if op == 'nao':
        break
if 'bia' not in pessoas_que_vao:
    print('bia nao vai, nao gostei, vou me jogar da ponte')
else:
    print('as pessoas que vao são',pessoas_que_vao)
    print('OPAAAA, BIA VAI, GOXTOOOOOO')