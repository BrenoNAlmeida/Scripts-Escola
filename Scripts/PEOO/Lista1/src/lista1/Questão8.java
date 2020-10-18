/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão8 {

    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        float n1, n2, n3, ma, me, in, tu;
        System.out.print("numero : ");
        n1 = num.nextFloat();
        System.out.print("numero : ");
        n2 = num.nextFloat();
        System.out.print("numero : ");
        n3 = num.nextFloat();
        tu = n1 + n2 + n3;
        if (n1 > n2 && n1 > n3) {
            ma = n1;
                if (n2 > n3) {
                    in = n2;
                    me = n3;
                }
                else {
                    in = n3;
                    me = n2;
                }
            System.out.printf("a ordem é %.2f , %.2f , %.2f\n",me,in,ma);
        } else if (n2 > n1 && n2 > n3) {
            ma = n2;
                if (n1 > n3) {
                    in = n1;
                    me = n3;
                }
                else {
                    in = n3;
                    me = n1;
                }
            System.out.printf("a ordem é %.2f , %.2f , %.2f\n",me,in,ma);
        } else if (n3 > n1 && n3 > n2) {
            ma = n3;
                if (n1 > n2) {
                    in = n1;
                    me = n2;
                } 
                else {
                    in = n2;
                    me = n1;
                }
            System.out.printf("a ordem é %.2f , %.2f , %.2f\n",me,in,ma);
        }

    }

}
