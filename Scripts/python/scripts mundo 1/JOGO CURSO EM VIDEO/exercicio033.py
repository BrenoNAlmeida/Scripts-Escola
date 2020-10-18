a = int(input('Primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
# verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando  quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('0 menor valor digitado foi {}'.format(menor))
print('0 maior valor digitado foi {}'.format(maior))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
