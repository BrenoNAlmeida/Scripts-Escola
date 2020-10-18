import random
n1=input('nome do 1° aluno :')
n2=input('nome do 2° aluno :')
n3=input('nome do 4° aluno :')
n4=input('nome do 4° aluno :')
g=[n1,n2,n3,n4]
sorteado= random.choice(g)
print('Dos alunos {} o aluno que vai apagar o quadro é {}'.format(g ,sorteado))