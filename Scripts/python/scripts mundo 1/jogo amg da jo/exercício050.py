v = 0
for leia in range(0,6):
    n = int(input('digite aqui um número inteiro: '))
    if n %  2 == 0:
        v += n
    else:
        print('desconsiderado')
if v == 0:
    print('não há números pares')
else:
    print(v)
print('fim')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break