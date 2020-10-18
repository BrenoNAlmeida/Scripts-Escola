print ("=== Bem vindo a Fase 1 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 1\n"
       "2. Desafio 2\n"
       "3. Desafio 3\n"
       "Qual desafio você escolhe?(digite um número de 1 a 3)")
num = int(input())
if num == 1:
    import D1
elif num == 2:
    import D2
elif num == 3:
    import D3
else:
    print("Inválido")