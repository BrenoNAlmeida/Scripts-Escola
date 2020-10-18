/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão7 {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        int num;
        System.out.println("numero : ");
        num = n.nextInt();
        if (num > 0 && num <= 9) {
            System.out.println("numero valido ");
        } else {
            System.out.println("numero invalido ");
        }

    }
}
