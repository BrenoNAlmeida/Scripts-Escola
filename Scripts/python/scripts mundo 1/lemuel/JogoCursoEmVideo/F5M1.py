print ("=== Bem vindo a Fase 5 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 22\n"
       "2. Desafio 23\n"
       "3. Desafio 24\n"
       "4. Desafio 25\n"
       "5. Desafio 26\n"
       "6. Desafio 27\n"
       "Qual desafio você escolhe?(digite um número de 1 a 6)")
num = int(input())
if num == 1:
    import D22
elif num == 2:
       import D23
elif num == 3:
       import D24
elif num == 4:
       import D25
elif num == 5:
       import D26
elif num == 6:
       import D27
else:
       print("Inválido")