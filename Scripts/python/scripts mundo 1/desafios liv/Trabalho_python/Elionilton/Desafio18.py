from math import radians, sin, cos, tan
a = float(input('Digite o ângulo para calcular: '))
ac = radians(a)
s = sin(ac)
c = cos(ac)
t = tan(ac)
print('O seno de {:.2f}º é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}!'.format(a, s, c, t), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio18', 'r')
    print(f.read())