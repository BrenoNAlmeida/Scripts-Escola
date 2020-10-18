print ("=== Bem vindo a Fase 2 do Mundo 2 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 66\n"
       "2. Desafio 67\n"
       "3. Desafio 68\n"
       "4. Desafio 69\n"
       "5. Desafio 70\n"
       "6. Desafio 71\n"
       "Qual desafio você escolhe?(digite um número de 1 a 6)")
num = int(input())

if num == 1:
    import D66
elif num == 2:
    import D67
elif num == 3:
    import D68
elif num == 4:
    import D69
elif num == 5:
    import D70
elif num == 6:
    import D71
else:
    print("Inválido")