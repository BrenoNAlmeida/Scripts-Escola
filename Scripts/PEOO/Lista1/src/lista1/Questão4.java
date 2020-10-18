/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão4 {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        float a, b, ma, me;
        System.out.print("numero : ");
        a = n.nextFloat();
        System.out.print("numero : ");
        b = n.nextFloat();
        if (a > b) {
            ma = a;
            me = b;
            System.out.printf("o maior numero é %.0f e o menor numero é %.0f", ma, me);
        } else if (b > a) {
            ma = b;
            me = a;
            System.out.printf("o maior numero é %.0f e o menor numero é %.0f", ma, me);
        } else {
            System.out.println("os numeros são iguais");
        }
    }

}
