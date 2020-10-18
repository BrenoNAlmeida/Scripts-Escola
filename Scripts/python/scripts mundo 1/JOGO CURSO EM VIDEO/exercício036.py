casa = float(input('valor dessa casa: R$'))
Salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos este pagamento? '))
prestação = casa / (anos * 12 )
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'. format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO! ')
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
