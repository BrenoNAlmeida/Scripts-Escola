/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/

package lista1;

import java.util.Scanner;

public class Questão1 {

    public static void main(String[] args) {
        Scanner en = new Scanner(System.in);
        float a, b, c, calc;
        System.out.print("numero : ");
        a = en.nextFloat();
        System.out.print("numero : ");
        b = en.nextFloat();
        System.out.print("numero : ");
        c = en.nextFloat();
        calc = b + c;
        if (a > calc) {
            System.out.println("O primeiro é maior do que a soma dos dois ultimos !!");
        } else {
            System.out.println("o primeiro NÃO é maior do que a somo dos sois ultimos");
        }

    }

}
