import random
n1=input('nome do 1° aluno:')
n2=input('nome do 2° aluno:')
n3=input('nome do 3° aluno:')
n4=input('nome do 4° aluno:')
L=[n1 , n2 , n3 ,n4]
random.shuffle(L)
print('a ordem de apresentação é :\n{}'.format(L))
