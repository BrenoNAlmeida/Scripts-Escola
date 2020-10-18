largura = float(input('Largura de parede: '))
alt = float(input('Altura da parede: '))
área = largura * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de{}m².'.format(largura, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisa de {}l de tinta.'.format(tinta))
opcao4 = ''
while opcao4!= 'S' and opcao4 != 'N':
    opcao4 = str(input('você deseja executar novamente [S/N]?')).upper()[0]
    if opcao4 == 'S':
        import JOGO
    if opcao4 == 'N':
        print('obrigado por ultilizar nossos serviços')
        break
