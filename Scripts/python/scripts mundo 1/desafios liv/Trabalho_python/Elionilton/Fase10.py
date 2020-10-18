print ("=== Bem vindo a Fase 2 do Mundo 2 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "66. Desafio 66\n"
       "67. Desafio 67\n"
       "68. Desafio 68\n"
       "69. Desafio 69\n"
       "70. Desafio 70\n"
       "71. Desafio 71\n"
       "Qual desafio você escolhe?(digite um número de 1 a 6)")
num = int(input())

if num == 66:
    import Desafio66
elif num == 67:
    import Desafio67
elif num == 68:
    import Desafio68
elif num == 69:
    import Desafio69
elif num == 70:
    import Desafio70
elif num == 71:
    import Desafio71
else:
    print("Inválido")