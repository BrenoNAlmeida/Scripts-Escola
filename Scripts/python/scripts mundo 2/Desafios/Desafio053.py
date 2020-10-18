print('\033[34m DETECTOR DE PALÍNDROMO\033[m')
frase = input('digite uma frase = ')
tirar = frase.replace(' ', '')
reverte = frase[::-1]
tira_revertido = reverte.replace(' ', '')
print(' a frase {} revertida é {}'.format(tirar, reverte))
if tirar == tira_revertido:
    print('a frase é um palindromo')
else:
    print('a frase nao é um palindromo')
