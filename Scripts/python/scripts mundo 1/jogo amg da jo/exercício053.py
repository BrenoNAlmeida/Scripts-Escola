#exercício053
fra = str(input('digite aqui uma frase: ')).strip().upper()
print('vamos verificar se sua frase é um palíndromo')
palavras = fra.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)- 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('palindromo')
else:
    print('não é palíndromo')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
