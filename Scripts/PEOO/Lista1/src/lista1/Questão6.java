/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

 */
package lista1;

import java.util.Scanner;

public class Questão6 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float n1, n2, n4, n5, frac1, frac2, sub, div, mult, soma;
        int n3;
        System.out.println("digite dois valores, como uma fração\n numerador:");
        n1 = sc.nextFloat();
        System.out.println("denominador");
        n2 = sc.nextFloat();
        System.out.println("a outra fração\n numerador:");
        n4 = sc.nextFloat();
        System.out.println("denominador");
        n5 = sc.nextFloat();
        frac1 = (n1 / n2);
        frac2 = (n4 / n5);
        System.out.println("qual operação você quer fazer com as frações");
        System.out.println("Subtração, digite 1");
        System.out.println("Divisão, digite 2");
        System.out.println("multiplicação, digite 3");
        System.out.println("soma, digite 4");
        n3 = sc.nextInt();
        switch (n3) {
            case (1):
                if (frac1 > frac2) {
                    sub = (frac1 - frac2);
                    System.out.printf("o resultado da subtração é " + sub);
                    if (frac2 > frac1) {
                        sub = (frac2 - frac1);
                        System.out.printf("O resultado da subtração é " + sub);
                    }
                }
                break;
            case (2):
                if (frac1 > frac2) {
                    div = (frac1 / frac2);
                    System.out.printf("o resultado da divisão é " + div);
                    if (frac2 > frac1) {
                        div = (frac2 / frac1);
                        System.out.printf("O resultado da divisão é " + div);
                    }
                }
                break;
            case (3):
                mult = (frac1 * frac2);
                System.out.printf("o resultado da multiplicação das frações é " + mult);
                break;
            case (4):
                soma = (frac1 + frac2);
                System.out.printf("o resultado da soma é " + soma);
                break;
            default:
                System.out.printf("opção não disponível, bb");
                break;
        }
    }

}
    


