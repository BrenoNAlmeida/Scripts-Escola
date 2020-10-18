print("=== Bem Vindo ao Mundo 2 - Gelo ===\n"
      "=== As fases desse mundo são ===\n"
      "7. Condições aninhadas\n"
      "8. Estrutura de repetição for\n"
      "9. Estrutura de repetição while\n"
      "10. Interropendo repetições while\n")
print("Qual fase você escolhe(número de 7 a 10)")
num = int(input())

if num == 7:
    import Fase7
elif num == 8:
    import Fase8
elif num == 9:
    import Fase9
elif num == 10:
    import Fase10
else:
    print("Inválido")