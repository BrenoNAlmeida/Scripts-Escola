import random
n1=input('nome do 1° aluno :')
n2=input('nome do 2° aluno :')
n3=input('nome do 4° aluno :')
n4=input('nome do 4° aluno :')
g=[n1,n2,n3,n4]
sorteado= random.choice(g)
print('Dos alunos {} o aluno que vai apagar o quadro é {}'.format(g ,sorteado))
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break