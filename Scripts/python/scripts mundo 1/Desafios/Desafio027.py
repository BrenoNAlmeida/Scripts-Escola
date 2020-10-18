nome=str(input('digite seu nome completo =')).capitalize()
trans=nome.split()
print('seu primeiro nome é {}'.format(trans[0]))
print('e seu ultimo nome é {}'.format(trans[len(trans)-1] ))