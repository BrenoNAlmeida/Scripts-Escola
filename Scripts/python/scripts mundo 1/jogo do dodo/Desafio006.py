n=int(input('\033[33;1mdigite um numero :\033[m '))
ra=n**(1/2)
d=n*2
t=n*3
letras = {'limpa': '\033[m',
        'azul':'\033[34m',
        'vermelho':'\033[31m',
        'verde':'\033[32m'}
print('O dobro de {}{} é :{}{}{}'.format(letras['verde'],n,letras['vermelho'],d,letras['limpa']))
print('O triplo de {}{} é :{}{}{}'.format(letras['verde'],n,letras['vermelho'],t,letras['limpa']))
print('A raiz quadrada de {}{} é : {}{}{}'.format(letras['verde'],n,letras['vermelho'],ra,letras['limpa']))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break