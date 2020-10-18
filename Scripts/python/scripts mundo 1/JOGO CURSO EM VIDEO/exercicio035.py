print('-='*20)
print('Analizador de triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('segundo segmento '))
r3 = float(input('terceiro seggmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmnetos PODEM FORMAR triangulos!')
else:
    print('Os segmnetos NÃO PODEM FORMAR triangulos!')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
