print('calcule a sua media anual !')
n1=float(input('primeira nota ='))
n2=float(input('segunda nota ='))
n3=float(input('terceira nota ='))
n4=float(input('querta nota ='))
m=(n1+n2+n3+n4)/4
print(' a sua media anual é {:.1f}'.format(m))
if m >= 6.0:
    print('aprovado')
else:
    print('reprovado')


