import math
a =float(input('Digite um angulo : '))
r=math.radians(a)
s= math.sin(r)
c= math.cos(r)
t= math.tan(r)
print('O seno de {} é {:.2}\nO cosceno de {} é {:.2}'.format(a,s,a,c))
print('a tangente de {} é {:.2}'.format(a,t))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break