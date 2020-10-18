idades = 0
idade_velha = 0
pessoa_velha = ''
menos_vinte = 0
for h in range(1,5):
    print('=== {}° pessoa==='.format(h))
    nome = input('Nome: ')
    idade = int(input('idade: '))
    sexo = input('Sexo [M/F]: ')
    idades += idade
    if h == 1 and sexo in 'Mm':
        idade_velha = idade
        pessoa_velha = nome
    if sexo in 'Mm' and idade > idade_velha:
        idade_velha = idade
        pessoa_velha = nome
    if sexo in 'Ff' and idade < 20:
        menos_vinte += 1
media = idades / 4
print('a media das idades das pessoas é {}'.format(media))
print('o homen mais velho tem {} anos e se chama {}'.format(idade_velha , pessoa_velha))
print('ao todo são {} mulheres com menos de 20 anos'.format(menos_vinte))