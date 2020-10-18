from playsound import playsound
playsound('musica.mp3')

cf = str(input("Você deseja ver o codigo fonte?(sim ou não)"))
if cf == "sim":
    f = open('D21', 'r')
    print(f.read())
