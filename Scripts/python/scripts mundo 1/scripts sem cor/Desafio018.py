import math
a =float(input('Digite um angulo : '))
r=math.radians(a)
s= math.sin(r)
c= math.cos(r)
t= math.tan(r)
print('O seno de {} é {:.2}\nO cosceno de {} é {:.2}'.format(a,s,a,c))
print('a tangente de {} é {:.2}'.format(a,t))