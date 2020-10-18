print("=== Jogo Curso Python Básico ===")
print("=== Os mundos desse jogo são===")
print("1. Mundo 1 - Floresta")
print("2. Mundo 2 - Gelo")
print("Qual mundo você escolhe(digite 1 ou 2)?")
num = int(input())
if num == 1:
    import Mundo1
elif num == 2:
    import Mundo2
else:
    print("Inválido")