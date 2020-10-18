/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão3 {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        float a, b, maior, menor, calc;
        System.out.print("numero : ");
        a = n.nextFloat();
        System.out.print("numero : ");
        b = n.nextFloat();
        if (a > b) {
            maior = a;
            menor = b;
        } else {
            maior = b;
            menor = a;
        }
        calc = maior - menor;
        System.out.printf("a diferença entre %.0f e %.0f é %.0f", a, b, calc);

    }
}
