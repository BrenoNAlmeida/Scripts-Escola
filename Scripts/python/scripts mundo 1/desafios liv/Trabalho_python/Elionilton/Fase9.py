print ("=== Bem vindo a Fase 2 do Mundo 2 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "57. Desafio 57\n"
       "58. Desafio 58\n"
       "59. Desafio 59\n"
       "60. Desafio 60\n"
       "61. Desafio 61\n"
       "62. Desafio 62\n"
       "63. Desafio 63\n"
       "64. Desafio 64\n"
       "65. Desafio 65\n"
       "Qual desafio você escolhe?(digite um número de 1 a 9)")
num = int(input())

if num == 57:
    import Desafio57
elif num == 58:
    import Desafio58
elif num == 59:
    import Desafio59
elif num == 60:
    import Desafio60
elif num == 61:
    import Desafio61
elif num == 62:
    import Desafio62
elif num == 63:
    import Desafio63
elif num == 64:
    import Desafio64
elif num == 65:
    import Desafio65
else:
    print("Inválido")

