/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

 */
package lista1;

import java.util.Scanner;

public class Questão9 {

    public static void main(String[] args) {
        Scanner en = new Scanner(System.in);
        float a;
        float calc1, calc2;
        System.out.print("digite um ano  ");
        a = en.nextFloat();
        calc1 = a % 4;
        calc2 = a % 400;
        if (calc1 != 0 && calc2 != 0) {
            System.out.printf("o ano %.0f NÃO é bixesto ", a);
        } else {
            System.out.printf("o ano %.0f é bixesto", a);
        }

    }

        
       
        
        
        
        
    
}
