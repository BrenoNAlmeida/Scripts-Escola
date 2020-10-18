print("\033[32m=== Bem vindo a fase 2 do mundo 1 ===\n"
      "=== Os desafios dessa fase são ===\n"
      "3. Desafio 3\n"
      "4. Desafio 4\n\033[33m"
      "Qual desafio você escolhe?(digite 3 ou 4)\033[31m")
num = int(input())
if num == 3:
    import Desafio3
elif num == 4:
    import Desafio4
else:
    print("Inválido")