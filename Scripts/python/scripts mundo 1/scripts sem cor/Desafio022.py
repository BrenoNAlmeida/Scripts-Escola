nome=input('digite seu nome completo =')
nomeup=nome.upper()
nomelo=nome.lower()
nomese=nome.strip()
dividido=nome.split()
print('em maiusculas = {}'.format(nomeup.strip()))
print('em minusculas = {}'.format(nomelo.strip()))
print('o seu nome tem {} letras'.format(len(nomese)-nomese.count(' ')))
print('o seu primeiro nome tem {}'.format(len(dividido[0])))
print(len(nomese))