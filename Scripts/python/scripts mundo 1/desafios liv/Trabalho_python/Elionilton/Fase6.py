print ("=== Bem vindo a Fase 6 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "28. Desafio 28\n"
       "29. Desafio 29\n"
       "30. Desafio 30\n"
       "31. Desafio 31\n"
       "32. Desafio 32\n"
       "33. Desafio 33\n"
       "34. Desafio 34\n"
       "35. Desafio 35\n"
       "Qual desafio você escolhe?(digite um número de 1 a 8)")
num = int(input())

if num == 28:
       import Desafio28
elif num == 29:
       import Desafio29
elif num == 30:
       import Desafio30
elif num == 31:
       import Desafio31
elif num == 32:
    import Desafio32
elif num == 33:
    import Desafio33
elif num == 34:
    import Desafio34
elif num == 35:
    import Desafio35
else:
    print("Inválido")