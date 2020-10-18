num = int(input('qual numero você deseja o fatorial ? '))
n = num
f = 1
while n > 0:
    print(' {} '.format(n), end=' ')
    print(' X ' if n > 1 else ' = ', end=' ')
    f *= n
    n -= 1
print(f)
