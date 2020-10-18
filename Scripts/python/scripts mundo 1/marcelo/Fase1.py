print ("\033[32m=== Bem vindo a Fase 1 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 1\n"
       "2. Desafio 2\033[33m\n"
       "Qual desafio você escolhe?(digite um número de 1 ou 2)\033[31m")
num = int(input())
if num == 1:
    import Desafio1
elif num == 2:
    import Desafio2
else:
    print("Inválido")