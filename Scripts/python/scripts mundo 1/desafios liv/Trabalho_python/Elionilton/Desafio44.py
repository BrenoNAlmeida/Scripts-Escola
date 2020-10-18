produto = float(input('Qual é o preço normal do produto? R$ '))
print('Qual será o método de pagamento?')
print('Para pagamento à vista em dinheiro/cheque (10% de desconto), digite 1.')
print('Para pagamento à vista no cartão de crédito (5% de desconto), digite 2.')
print('Para pagamento parcelado em até 12x no cartão de crédito (20% de juros a partir de 3x), digite 3.')
pagamento = int(input('Digite a opção desejada: '))
if pagamento == 1:
    valor = produto - (produto * 10 / 100)
    print('O produto à vista em dinheiro/cheque, com 10% de desconto,', end=' ')
    print('fica de R$ {:.2f} por R$ {:.2f}!\n'.format(produto, valor))
elif pagamento == 2:
    valor = produto - (produto * 5 / 100)
    print('O produto à vista no cartão de crédito, com 5% de desconto,', end=' ')
    print('fica de R$ {:.2f} por R$ {:.2f}!\n'.format(produto, valor))
elif pagamento == 3:
    parcelas = int(input('Em quantas vezes deseja parcelar? Digite um número de 2 a 12: '))
    if parcelas == 1:
        valor = produto - (produto * 5 / 100)
        print('O produto à vista no cartão de crédito, com 5% de desconto,', end=' ')
        print('fica de R$ {:.2f} por R$ {:.2f}\n!'.format(produto, valor))
    elif parcelas == 2:
        valor = produto
        par = valor / parcelas
        print('O produto parcelado em 2x de R$ {:.2f} no cartão de crédito,'.format(par), end=' ')
        print('sem nenhum desconto, continua por R$ {:.2f}!\n'.format(produto))
    elif 2 < parcelas <= 12:
        valor = produto + (produto * 20 / 100)
        par = valor / parcelas
        print('O produto parcelado em {}x de R$ {:.2f} no cartão de crédito,'.format(parcelas, par), end=' ')
        print('com 20% de juros, fica de R$ {:.2f} por R$ {:.2f}!\n'.format(produto, valor))
    else:
        print('Número inválido de parcelas! Digite um número de 2 a 12.\n')
else:
    print('Opção inválida! Digite um número de 1 a 3.\n')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio44', 'r')
    print(f.read())