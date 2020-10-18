/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão12 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s;
        float h, p;
        System.out.print("qual o seu sexo [F/M] ? ");
        s = sc.nextLine();
        s = s.toLowerCase();
        System.out.println("qual a sua altura ? ");
        h = sc.nextFloat();
        switch (s) {
            case "f":
                p = (float) ((62.1 * h) - 44.7);
                System.out.printf("seu peso ideal é %.3f", p);
            case "m":
                p = (float) ((72.7 * h) - 58);
                System.out.printf("seu peso ideal é %.3f", p);
            default:
                System.out.println("sexo invalido, execute novamente !");
        }

    }
}
