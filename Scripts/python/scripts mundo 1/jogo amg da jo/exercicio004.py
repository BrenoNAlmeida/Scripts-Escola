algo=input('Digite algo = ')
print('o que você digitou :')
print('é um formato primitivo :{}'.format(type(algo)))
print('O que vocé digitou são apenas numeros ?',algo.isnumeric())
print('O que vocé digitou são apenas letras ?',algo.isalpha())
print('O que vocé digitou são numeros e letras',algo.isalnum())
print('as letras estão todas maiusculas ?',algo.isupper())
print('as letras estão todas minusculas ?',algo.islower())
print('oa caracteres são imprimiveis ? ',algo.isprintable())
print('são apenas espaços ? ',algo.isspace())
print('são todos digitos ?',algo.isdigit())
print('são todos caracteres decimais ?',algo.isdecimal())
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break