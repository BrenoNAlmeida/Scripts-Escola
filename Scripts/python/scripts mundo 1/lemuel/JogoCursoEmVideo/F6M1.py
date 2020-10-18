print ("=== Bem vindo a Fase 6 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 28\n"
       "2. Desafio 29\n"
       "3. Desafio 30\n"
       "4. Desafio 31\n"
       "5. Desafio 32\n"
       "6. Desafio 33\n"
       "7. Desafio 34\n"
       "8. Desafio 35\n"
       "Qual desafio você escolhe?(digite um número de 1 a 8)")
num = int(input())

if num == 1:
       import D28
elif num == 2:
       import D29
elif num == 3:
       import D30
elif num == 4:
       import D31
elif num == 5:
    import D32
elif num == 6:
    import D33
elif num == 7:
    import D34
elif num == 8:
    import D35
else:
    print("Inválido")