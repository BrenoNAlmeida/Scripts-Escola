distancia = float(input('Digite a distância em Km da sua viagem (ex: 228.5): '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem para uma viagem de {} Km vai custar R$ {:.2f}!'.format(distancia, passagem), "\n")
else:
    passagem = distancia * 0.45
    print('Sua passagem para uma viagem de {} Km vai custar R$ {:.2f}!'.format(distancia, passagem), "\n")

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio31', 'r')
    print(f.read())