algo=str(input('digite algo =')).strip()
trans=algo.lower()
conte=trans.count('a')
print('no que você digitou tem {} letras A'.format(conte))
print('a primeira letra a começa na posição {} '.format(algo.find('a')+1))
print('e a ultima na posiçao {}'.format(algo.rfind('a')+1))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break