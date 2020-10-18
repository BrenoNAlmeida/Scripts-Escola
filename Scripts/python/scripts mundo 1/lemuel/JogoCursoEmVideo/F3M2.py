print ("=== Bem vindo a Fase 2 do Mundo 2 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 57\n"
       "2. Desafio 58\n"
       "3. Desafio 59\n"
       "4. Desafio 60\n"
       "5. Desafio 61\n"
       "6. Desafio 62\n"
       "7. Desafio 63\n"
       "8. Desafio 64\n"
       "9. Desafio 65\n"
       "Qual desafio você escolhe?(digite um número de 1 a 9)")
num = int(input())

if num == 1:
    import D57
elif num == 2:
    import D58
elif num == 3:
    import D59
elif num == 4:
    import D60
elif num == 5:
    import D61
elif num == 6:
    import D62
elif num == 7:
    import D63
elif num == 8:
    import D64
elif num == 9:
    import D65
else:
    print("Inválido")

