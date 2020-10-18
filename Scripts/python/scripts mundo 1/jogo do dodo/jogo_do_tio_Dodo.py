from time import sleep
print('\033[32m BEM VINDO A BIBLIOTECA DO CURSO EM VIDEO PEQUENO GAFANHOTO\033[m')
print('1  - MUNDO 1 -  FLORESTA\n'
      '2  - MUNDO 2 -   GELO')
mundo = int(input('Qual mundo você deseja '))
if mundo == 1:
    print('em precessamento...')
    sleep(3)
    import mundo1
if mundo == 2:
    print('em precessamento...')
    sleep(3)
    import mundo2