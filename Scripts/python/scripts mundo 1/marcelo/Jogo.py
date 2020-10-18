print("\033[31m=== Jogo Curso Python Básico ===")
print("=== Os mundos desse jogo são===\033[32m")
print("1. Mundo 1 - Floresta\033[34m")
print("2. Mundo 2 - Gelo\033[33m")
print("Qual mundo você escolhe(digite 1 ou 2)?")
num = int(input())
if num == 1:
    import Mundo1
elif num == 2:
    import Mundo2
else:
    print("Inválido")