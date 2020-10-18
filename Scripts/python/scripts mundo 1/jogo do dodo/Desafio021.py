from pygame import *
print('a musica será executada em breve')
mixer.init()
mixer.music.load('Desafio021.mp3')
mixer.music.play()
print('tocando...')
while mixer.music.get_busy():
    time.Clock().tick(10)
print('a musica acabou !!!')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break