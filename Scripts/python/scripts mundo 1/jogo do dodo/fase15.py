print('\033[34mOs desafios dessa fase são essas :\n'
      '66 = varios numeros com flag\n'
      '67 = tabuada 3.0\n'
      '68 = GAME  par ou impar\n'
      '69 = cadastro de pessoas  2.0\n'
      '70 = loja super baratão\n'
      '71 = caixa eletronico\033[m\n')
desafio = int(input('qual fase você deseja ?'))
if desafio == 66:
    import Desafio66
if desafio == 67:
    import Desafio067
if desafio == 68:
    import Desafio068
if desafio == 69:
    import Desafio069
if desafio == 70:
    import Desafio070
if desafio == 71:
    import Desafio071
