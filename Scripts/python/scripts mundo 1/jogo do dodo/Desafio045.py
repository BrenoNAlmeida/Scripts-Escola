from random import choice
print('\033[31m VAMOS JOGAR JOKENPÔ\033[m')
vdc = input('O que você quer :\n'
      'pedra , papel ou tesoura ?')
agora_vai = ['pedra','papel','tesoura']
amo_adorilson = choice(agora_vai)
if amo_adorilson == vdc:
    print('eita , eu também escolhi {}'.format(amo_adorilson))
elif vdc == 'pedra' and amo_adorilson == 'tesoura':
    print('droga você ganhou , eu escolhi {}'.format(amo_adorilson))
elif vdc == 'papel' and amo_adorilson == 'pedra':
    print('droga você ganhou , eu escolhi {}'.format(amo_adorilson))
elif vdc == 'tesoura' and amo_adorilson == 'papel':
    print('droga você ganhou , eu escolhi {}'.format(amo_adorilson))
elif vdc == 'pedra' and amo_adorilson == 'papel':
    print('droga você ganhou , eu escolhi {}'.format(amo_adorilson))
elif amo_adorilson == 'papel' and vdc == 'pedra':
    print('HA HA , eu ganhei bb, escolhi {}'.format(amo_adorilson))
elif amo_adorilson == 'pedra' and vdc == 'tesoura':
    print('HA HA , eu ganhei bb, escolhi {}'.format(amo_adorilson))
elif amo_adorilson == 'tesoura' and vdc == 'papel':
    print('HA HA , eu ganhei bb, escolhi {}'.format(amo_adorilson))
elif amo_adorilson == 'pedra' and vdc == 'papel':
    print('HA HA , eu ganhei bb, escolhi {}'.format(amo_adorilson))
else:
    print('ERRO, execute novamente ')
print('\033[34m VAMOS JOGAR NOVAMENTE PEQUENO GAFANHOTO\033[m')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break