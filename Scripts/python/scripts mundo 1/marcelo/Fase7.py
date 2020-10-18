print ("\033[34m=== Bem vindo a Fase 1 do Mundo 2 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "36. Desafio 36\n"
       "37. Desafio 37\n"
       "38. Desafio 38\n"
       "39. Desafio 39\n"
       "40. Desafio 40\n"
       "41. Desafio 41\n"
       "42. Desafio 42\n"
       "43. Desafio 43\n"
       "44. Desafio 44\n"
       "45. Desafio 45\033[36m\n"
       "Qual desafio você escolhe?(digite um número de 1 a 10)\033[31m")
num = int(input())

if num == 36:
    import Desafio36
elif num == 37:
    import Desafio37
elif num == 38:
    import Desafio38
elif num == 39:
    import Desafio39
elif num == 40:
    import Desafio40
elif num == 41:
    import Desafio41
elif num == 42:
    import Desafio42
elif num == 43:
    import Desafio43
elif num == 44:
    import Desafio44
elif num == 45:
    import Desafio45
else:
    print("Inválido")