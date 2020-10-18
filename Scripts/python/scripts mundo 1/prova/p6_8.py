curso = ''
def ifcm (curso):
    while True:
        curso = str(input('curso = ')).upper()
        if curso == 'INFO':
            print('Informática \n Tenha bons estudos')
            break
        if curso == 'EBM':
            print('Manutenção em Equipamentos Biomédicos \n Tenha bons estudos')
            break
        if curso == 'PJD':
            print('Programação em Jogos Digitais \n você escolheu o melhor curso do campus \n Tenha bons estudos')
            break
    return curso
print(ifcm(curso))