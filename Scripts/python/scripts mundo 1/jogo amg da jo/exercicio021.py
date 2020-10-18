from pygame import *

mixer.init()
mixer.music.load('exercicio021.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import JOGO
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break