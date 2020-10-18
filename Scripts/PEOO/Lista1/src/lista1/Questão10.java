/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/


package lista1;

import java.util.Scanner;

public class Questão10 {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        int n1;
        System.out.print("digite um numero");
        n1 = n.nextInt();
        if (n1 < 3);
        switch (n1) {
            case 1:
                System.out.println("um");
                break;
            case 2:
                System.out.println("dois");
                break;
            case 3:
                System.out.println("três");
                break;
            default:
                System.out.println("numero invalido");
        }

    }
}
