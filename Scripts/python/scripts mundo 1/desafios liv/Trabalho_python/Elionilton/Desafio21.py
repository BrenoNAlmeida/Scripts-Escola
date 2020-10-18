from playsound import playsound
playsound('musica.mp3')

cf = str(input("Você deseja ver o codigo fonte?"))
if cf == "sim" or "s" or "Sim":
    f = open('Desafio21', 'r')
    print(f.read())
