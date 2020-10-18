#exercício056
old = 0
id = 0
gi = 0
maioridade = 0
for gp in range (1,5):
    nom = str(input('qual o seu nome? '))
    n = int(input('qual a sua idade? '))
    sex = int(input('''qual o seu sexo? 
    [ 1 ] - masculino
    [ 2 ] - feminino 
    digite aqui sua escolha: '''))
    if sex == 2:
        if n < 20:
            gi += 1
    if sex == 1:
        if n > maioridade:
            maioridade = n
            old = nom
    id += n
med = ((id)/(4))
print('a média de idades é {:0.0f} years old.'.format(med))
if gi > 1:
    print('existem {} mulheres com menos de 20 anos'.format(gi))
if gi == 1:
    print('existe {} mulher com menos de 20 anos'.format(gi))
if gi < 1:
    print('não existem mulheres com mennos de 20 anos')
print('o homem mais velho é {} e ele tem {} anos. rs'.format(old, maioridade))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break