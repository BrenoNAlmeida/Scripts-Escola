from pygame import *
print('''as musicas dessa biblioteca são:
[ 1 ] = paradise.mp3
[ 2 ] = miracles.mp3
[ 3 ] = Radioctive.mp3
[ 4 ] = mocinho do cinema
[ 5 ] = amuleto ''')
musica = int(input('qual musica você deseja [ apenas numero ] ?'))
if musica == 1:
    print('a musica será executada em breve')
    mixer.init()
    mixer.music.load('paradise.mp3')
    mixer.music.play()
    print('tocando...')
    while mixer.music.get_busy():
        time.Clock().tick(10)
    print('a musica acabou !!!')
if musica == 2:
    print('a musica será executada em breve')
    mixer.init()
    mixer.music.load('miracles.mp3')
    mixer.music.play()
    print('tocando...')
    while mixer.music.get_busy():
        time.Clock().tick(10)
    print('a musica acabou !!!')
if musica == 3:
    print('a musica será executada em breve')
    mixer.init()
    mixer.music.load('Radioactive.mp3')
    mixer.music.play()
    print('tocando...')
    while mixer.music.get_busy():
        time.Clock().tick(10)
    print('a musica acabou !!!')
if musica == 4:
    print('a musica será executada em breve')
    mixer.init()
    mixer.music.load('Mocinho_do_cinema.mp3')
    mixer.music.play()
    print('tocando...')
    while mixer.music.get_busy():
        time.Clock().tick(10)
    print('a musica acabou !!!')
if musica == 5:
    print('a musica será executada em breve')
    mixer.init()
    mixer.music.load('amuleto.mp3')
    mixer.music.play()
    print('tocando...')
    while mixer.music.get_busy():
        time.Clock().tick(10)
    print('a musica acabou !!!')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import Biblioteca_de_musicas
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break
