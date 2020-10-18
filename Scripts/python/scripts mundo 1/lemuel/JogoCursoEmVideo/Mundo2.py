print("=== Bem Vindo ao Mundo 2 - Gelo ===\n"
      "=== As fases desse mundo são ===\n"
      "1. Condições aninhadas\n"
      "2. Estrutura de repetição for\n"
      "3. Estrutura de repetição while\n"
      "4. Interropendo repetições while\n")
print("Qual fase você escolhe(número de 1 a 4)")
num = int(input())

if num == 1:
    import F1M2
elif num == 2:
    import F2M2
elif num == 3:
    import F3M2
elif num == 4:
    import F4M2
else:
    print("Inválido")
