print("\033[32m=== Bem vindo a Fase 5 do Mundo 1 ===\n"
      "=== Os desafios dessa fase são ===\n"
      "22. Desafio 22\n"
      "23. Desafio 23\n"
      "24. Desafio 24\n"
      "25. Desafio 25\n"
      "26. Desafio 26\n"
      "27. Desafio 27\n\033[33m"
      "Qual desafio você escolhe?(digite um número de 22 a 27)\033[31m")
num = int(input())
if num == 22:
    import Desafio22
elif num == 23:
    import Desafio23
elif num == 24:
    import Desafio24
elif num == 25:
    import Desafio25
elif num == 26:
    import Desafio26
elif num == 27:
    import Desafio27
else:
    print("Inválido")
