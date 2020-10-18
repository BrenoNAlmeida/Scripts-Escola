
package lista3;

import java.util.Scanner;


public class Ques3 {
     public static void main(String[] args) {
        int idade [] = new int [10];
        int cont= 0 ;
        Scanner xx = new Scanner(System.in);
        for ( int i = 0; i <= 9; i++){
            System.out.println("Digite a idade: ");
            idade [i] = xx.nextInt();
            }
        for(int c = 0; c <= idade.length;c++)
                    if (idade[c] == 18){
                cont = cont + 1;
                    }
        System.out.println(" A quantidade de pessoas que posssuíem 18 anos é  " + cont);
    }
    
}
