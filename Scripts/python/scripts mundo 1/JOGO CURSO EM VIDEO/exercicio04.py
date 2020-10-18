a = input('Digite algo: ')
print('5 tipo primitivo dese valor', type(a))
print('É um numero?', a.isnumeric())
print('Só tem espaços?', a.isspace())
print( 'Está capitalizada? ', a.istitle())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print ('Está em maiusculas? ', a.isupper())
print('Está em minuscula? ', a.islower())

opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
