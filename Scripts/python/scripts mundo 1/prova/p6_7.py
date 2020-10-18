bat = int(input('bateria = '))
def batery (bat):
    if bat == 0:
        print('morri')
    elif bat > 0 and bat < 21:
        print('conecte o carreador')
    elif bat > 20 and bat < 80:
        print('carregando...')
    elif bat > 79 and bat < 100:
        print('estou de boa')
    elif bat == 100:
        print('pode tirar o carregador')
    elif bat > 100:
        print('estou ligadasso')
    return bat


print(batery(bat))
batery(bat)

