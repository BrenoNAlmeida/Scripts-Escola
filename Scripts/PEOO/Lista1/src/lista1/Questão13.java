/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão13 {

    public static void main(String[] args) {
        Scanner en = new Scanner(System.in);
        float a, b, calc;
        int op;
        System.out.print("numero : ");
        a = en.nextFloat();
        System.out.print("numero : ");
        b = en.nextFloat();
        System.out.println("as operações disponiveis são : \n"
                + "[1] = soma\n"
                + "[2] = multiplicação\n"
                + "[3] = divisão\n"
                + "[4] = subtração\n");
        System.out.print("Qual operação você deseja fazer ? ");
        op = en.nextInt();
        switch (op) {
            case 1:
                calc = a + b;
                System.out.printf("a soma é igual a %.2f ", calc);
                break;
            case 2:
                calc = a * b;
                System.out.printf("a multiplicaçao é igual a %.2f ", calc);
                break;
            case 3:
                calc = a / b;
                System.out.printf(" %.2f dividido por %.2f é igual a %.2f", a, b, calc);
                break;
            case 4:
                calc = a - b;
                System.out.printf("%.2f menos %.2f é igual a %.2f", a, b, calc);
                break;
            default:
                System.out.println("operação invalida, execute novamente !");

        }

    }

}
