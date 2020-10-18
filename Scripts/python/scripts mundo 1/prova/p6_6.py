import math
def calc (l , a ,ar):
    calc = (l * a) / (ar /100)
    return calc
l = int(input())
a = int(input())
ar = int(input())
print(math.ceil(calc(l,a,ar)))