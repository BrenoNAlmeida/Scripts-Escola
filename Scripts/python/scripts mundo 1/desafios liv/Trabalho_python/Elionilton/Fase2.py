print("=== Bem vindo a fase 2 do mundo 1 ===\n"
      "=== Os desafios dessa fase são ===\n"
      "3. Desafio 3\n"
      "4. Desafio 4\n"
      "Qual desafio você escolhe?(digite 3 ou 4)")
num = int(input())
if num == 3:
    import Desafio3
elif num == 4:
    import Desafio4
else:
    print("Inválido")