print ("=== Bem vindo a Fase 1 do Mundo 2 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 36\n"
       "2. Desafio 37\n"
       "3. Desafio 38\n"
       "4. Desafio 39\n"
       "5. Desafio 40\n"
       "6. Desafio 41\n"
       "7. Desafio 42\n"
       "8. Desafio 43\n"
       "9. Desafio 44\n"
       "10. Desafio 45\n"
       "Qual desafio você escolhe?(digite um número de 1 a 10)")
num = int(input())

if num == 1:
    import D36
elif num == 2:
    import D37
elif num == 3:
    import D38
elif num == 4:
    import D39
elif num == 5:
    import D40
elif num == 6:
    import D41
elif num == 7:
    import D42
elif num == 8:
    import D43
elif num == 9:
    import D44
elif num == 10:
    import D45
else:
    print("Inválido")