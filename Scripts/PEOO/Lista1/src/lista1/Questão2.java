/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão2 {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        float a, b, calc;
        System.out.print("qual o ano que você nasceu ?");
        a = n.nextInt();
        System.out.print("qual o ano atual ? ");
        b = n.nextInt();
        calc = b - a;
        System.out.printf("você vai fazer %.0f anos em %.0f ", calc, b);
    }

}
