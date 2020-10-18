
package lista3;

import java.util.Scanner;


public class Q3 {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nome;        
        int idade;
        int addma = 0;
        int vetor [] = new int [10]; 
        for (int cont = 0; cont < vetor.length; cont++) {
            System.out.print("qual a sua idade ? ");
            idade = sc.nextInt();
            vetor[cont] =idade;
        }
        for (int i  = 0; i < vetor.length ;i++){
            if ( vetor[i]>= 18) {
            addma++;
            }

        }
        System.out.printf(" %d pessoas são maior de idade\n", addma);

    }
}
