print("\033[32;1m=== Bem Vindo ao Mundo 1 - Floresta ===\n"
      "=== As fases desse mundo são ===\n"
      "1. Primeiros Comandos em python\n"
      "2. Tipos Primitivos e Saída de Dados\n"
      "3. Operadores Aritméticos\n"
      "4. Utilizando Módulos\n"
      "5. Manipulando Strings\n"
      "6. Estrutura Condicional(Parte 1)\033[m\n")
print("\033[33mQual fase você escolhe(número de 1 a 6) ?\033[m")
num = int(input())

if num == 1:
    import Fase1
elif num == 2:
    import Fase2
elif num == 3:
    import Fase3
elif num == 4:
    import Fase4
elif num == 5:
    import Fase5
elif num == 6:
    import Fase6
else:
    print("Inválido")