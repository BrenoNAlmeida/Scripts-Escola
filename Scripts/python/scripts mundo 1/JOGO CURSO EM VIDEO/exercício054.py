from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 4):
    nasceu = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasceu
    if idade >= 18:
        totmaior +=1

    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E TAMBEM tivemos {} pessoas menores de idade'.format(totmenor))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
