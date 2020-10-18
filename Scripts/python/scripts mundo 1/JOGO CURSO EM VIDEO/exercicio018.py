from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que voce deseia: '))
seno = sin(radians(ângulo))
print('0 ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('0 ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tagente = tan(radians(ângulo))
print('0 ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tagente))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
