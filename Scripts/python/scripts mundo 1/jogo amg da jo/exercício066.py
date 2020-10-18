#exercício066
s = 0
cont = 0
n = float(input('''digite um valor aqui 
para parar, por favor digite 999, @ '''))
r = n
while n != 999:
    n = float(input('''digite um valor aqui 
    para parar, por favor digite 999, @ '''))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma entre os números que você digitou foi {s + r}')
if cont == 0:
    print(f'Você digitou apenas 1 número')
else:
    print(f'Você digitou {cont+1} números')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break