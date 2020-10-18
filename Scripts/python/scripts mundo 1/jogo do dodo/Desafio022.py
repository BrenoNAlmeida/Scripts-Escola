nome=input('digite seu nome completo =')
nomeup=nome.upper()
nomelo=nome.lower()
nomese=nome.strip()
dividido=nome.split()
print('em maiusculas = {}'.format(nomeup.strip()))
print('em minusculas = {}'.format(nomelo.strip()))
print('o seu nome tem {} letras'.format(len(nomese)-nomese.count(' ')))
print('o seu primeiro nome tem {}'.format(len(dividido[0])))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break