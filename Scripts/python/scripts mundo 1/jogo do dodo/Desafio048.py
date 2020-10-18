print('o somatorio de todos os numeros impares divisiveis por três entre 0 e 500 é')
for c in range(0,500):
   if c % 3 == 0 :
    algo = (c)
    soma = algo + c
print(soma)
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
k