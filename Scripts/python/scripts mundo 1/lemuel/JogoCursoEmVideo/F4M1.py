print ("=== Bem vindo a Fase 4 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 16\n"
       "2. Desafio 17\n"
       "3. Desafio 18\n"
       "4. Desafio 19\n"
       "5. Desafio 20\n"
       "6. Desafio 21\n"
       "Qual desafio você escolhe?(digite um número de 1 a 6)")
num = int(input())

if num == 1:
    import D16
elif num == 2:
    import D17
elif num == 3:
    import D18
elif num == 4:
    import D19
elif num == 5:
    import D20
elif num == 6:
    import D21
else:
    print("Inválido")