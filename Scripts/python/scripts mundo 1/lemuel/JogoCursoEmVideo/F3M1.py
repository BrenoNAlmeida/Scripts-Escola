print ("=== Bem vindo a fase 3 do mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 5\n"
       "2. Desafio 6\n"
       "3. Desafio 7\n"
       "4. Desafio 8\n"
       "5. Desafio 9\n"
       "6. Desafio 10\n"
       "7. Desafio 11\n"
       "8. Desafio 12\n"
       "9. Desafio 13\n"
       "10. Desafio 14\n"
       "11. Desafio 15\n"
       "Qual desafio você escolhe?(digite um número de 1 a 11)")
num = int(input())
if num == 1:
    import D5
elif num == 2:
    import D6
elif num == 3:
    import D7
elif num == 4:
    import D8
elif num == 5:
    import D9
elif num == 6:
    import D10
elif num == 7:
    import D11
elif num == 8:
    import D12
elif num == 9:
    import D13
elif num == 10:
    import D14
elif num == 11:
    import D15
else:
    print("Inválido")