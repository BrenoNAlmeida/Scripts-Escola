print('\033[31;4mconverta as temperaturas de °C em °F')
print('\033[32m=='*18)
c = float(input('\033[31minforme a temperatura em °C = \033[m'))
f = ((9 * c) / 5) + 32
print('\033[34mA temperatura \033[31m{}°C\033[34m é igual a \033[31m{}°F'.format(c, f))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break