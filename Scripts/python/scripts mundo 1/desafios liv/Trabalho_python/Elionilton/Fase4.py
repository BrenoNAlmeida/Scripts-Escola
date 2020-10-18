print ("=== Bem vindo a Fase 4 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "16. Desafio 16\n"
       "17. Desafio 17\n"
       "18. Desafio 18\n"
       "19. Desafio 19\n"
       "20. Desafio 20\n"
       "21. Desafio 21\n"
       "Qual desafio você escolhe?(digite um número de 16 a 21)")
num = int(input())

if num == 16:
    import Desafio16
elif num == 17:
    import Desafio17
elif num == 18:
    import Desafio18
elif num == 19:
    import Desafio19
elif num == 20:
    import Desafio20
elif num == 21:
    import Desafio21
else:
    print("Inválido")