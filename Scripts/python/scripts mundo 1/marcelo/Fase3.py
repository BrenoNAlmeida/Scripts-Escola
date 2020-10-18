print ("\033[32m=== Bem vindo a fase 3 do mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "5. Desafio 5\n"
       "6. Desafio 6\n"
       "7. Desafio 7\n"
       "8. Desafio 8\n"
       "9. Desafio 9\n"
       "10. Desafio 10\n"
       "11. Desafio 11\n"
       "12. Desafio 12\n"
       "13. Desafio 13\n"
       "14. Desafio 14\n"
       "15. Desafio 15\033[33m\n"
       "Qual desafio você escolhe?(digite um número de 5 a 15)\033[31m")
num = int(input())
if num == 5:
    import Desafio5
elif num == 6:
    import Desafio6
elif num == 7:
    import Desafio7
elif num == 8:
    import Desafio8
elif num == 9:
    import Desafio9
elif num == 10:
    import Desafio10
elif num == 11:
    import Desafio11
elif num == 12:
    import Desafio12
elif num == 13:
    import Desafio13
elif num == 14:
    import Desafio14
elif num == 15:
    import Desafio15
else:
    print("Inválido")