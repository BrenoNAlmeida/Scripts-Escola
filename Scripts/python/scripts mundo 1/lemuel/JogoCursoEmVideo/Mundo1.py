print("=== Bem Vindo ao Mundo 1 - Floresta ===\n"
      "=== As fases desse mundo são ===\n"
      "1. Primeiros Comandos em python\n"
      "2. Tipos Primitivos e Saída de Dados\n"
      "3. Operadores Aritméticos\n"
      "4. Utilizando Módulos\n"
      "5. Manipulando Strings\n"
      "6. Estrutura Condicional(Parte 1)\n")
print("Qual fase você escolhe(número de 1 a 6)")
num = int(input())

if num == 1:
    import F1M1
elif num == 2:
    import F2M1
elif num == 3:
    import F3M1
elif num == 4:
    import F4M1
elif num == 5:
    import F5M1
elif num == 6:
    import F6M1
else:
    print("Inválido")