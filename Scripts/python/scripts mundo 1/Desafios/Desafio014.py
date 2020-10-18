print('\033[31;4mconverta as temperaturas de °C em °F')
print('\033[32m=='*18)
c = float(input('\033[31minforme a temperatura em °C = \033[m'))
f = ((9 * c) / 5) + 32
print('\033[34mA temperatura \033[31m{}°C\033[34m é igual a \033[31m{}°F'.format(c, f))
