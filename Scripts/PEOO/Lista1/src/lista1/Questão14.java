/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão14 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, op;
        float calc;
        System.out.print("numero : ");
        a = sc.nextInt();
        System.out.print("numero : ");
        b = sc.nextInt();
        System.out.println("QUAL OPÇÃO VOCÊ DESEJA\n"
                + "[1] – Verificar se um dos números lidos é ou não múltiplo do outro\n"
                + "[2] – Verificar se os dois números lidos são pares\n"
                + "[3] – Verificar se a média dos dois números é maior ou igual a 7\n"
                + "[4] - sair do programa");
        System.out.print("qual opção você deseja ? ");
        op = sc.nextInt();
        switch (op) {
            case 1:
                calc = a % b;
                if (calc == 0) {
                    System.out.printf(" %d é multiplo de %d\n", a, b);
                    break;
                } else {
                    System.out.printf(" %d NÃO é multiplo de %d\n", a, b);
                    break;
                }
            case 2:
                if (a % 2 == 0 && b % 2 == 0) {
                    System.out.println("%d e %d são ambos pares\n");
                    break;
                } else if (a % 2 == 0 || b % 2 == 0) {
                    System.out.printf("%d ou %d um deles é par e o outro impar\n", a, b);
                    break;
                } else {
                    System.out.printf("%d e %d sao ambos impares\n", a, b);
                    break;
                }
            case 3:
                calc = (a + b) / 2;
                if (calc >= 7) {
                    System.out.printf("a media é = %.2f, a media é maior do que 7\n", calc);
                    break;
                } else {                    
                    System.out.printf("a media é = %.2f, a media é menor do que 7\n", calc);
                    break;
                }
            case 4:
                System.out.println("obrigado por executar nosso programa");
                break;
            default:
                System.out.println("opção invalida !");

        }
    }

}
