print('Gerador de PA')
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão de PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais, querido?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
