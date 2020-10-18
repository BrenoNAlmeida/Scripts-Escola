#exercício069
idade = 0
sexo = 0
con = 0
cont = 0
s = 0
m = 0
while True:
    idade = int(input('digite aqui sua idade: '))
    sexo = int(input('Seu sexo:\n[ 1 ] - Feminino\n[ 2 ] - Masculino'))
    if idade > 18:
        cont += 1
    if sexo == 2:
        s += 1
    if sexo == 1:
        if idade < 20:
            m += 1
    con = int(input('Você deseja continuar?\n[ 1 ] - Sim\n[ 2 ] - Não '))
    if con == 2:
        break
esg = '='
print(f'{esg*50}\n                  RESULTADOS')
if cont == 0:
    print('nenhuma  pessoa tem mais de 18 anos.')
if cont == 1:
    print('apenas {} tem mais de 18 anos.'.format(cont))
if cont > 1:
    print('{} pessoas tem mais de 18 anos.'.format(cont))
if s == 1:
    print('apenas um homem cadastrado.')
if s == 0:
    print('nenhum homem cadastrado')
if s > 1:
    print('{} homens cadastrados'.format(s))
if m == 0:
    print('nenhuma mulher com menos de 20 anos foi cadastrada')
if m == 1:
    print('apenas uma mulher com menos de 20 anos foi cadastrada')
if m > 1:
    print('{} mulheres menores de 20 anos foram cadastradas'.format(m))
print(f'{esg*50}')
escolha4 = ''
while escolha4 != 'sim' and escolha4 != 'nao':
    escolha4 = str(input('você deseja executar novamente [sim/nao]?')).lower()
    if escolha4 == 'sim':
        import jogo_do_tio_Dodo
    if escolha4 == 'nao':
        print('obrigado por ultilizar nossos serviços')
        break