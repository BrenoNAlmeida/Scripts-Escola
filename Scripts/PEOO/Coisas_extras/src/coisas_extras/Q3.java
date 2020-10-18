
package coisas_extras;

import java.util.Scanner;


public class Q3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int num = 1,ve ;
        while(num != 0){
            System.out.print("numero = ");
            num = sc.nextInt();
            ve = num % 7;
            if (ve == 0){
                System.out.printf("%d é multiplo de 7 \n [para sair digite 0]",num);
            }
            else{
                System.out.printf("%d NÃO é multiplo de 7 \n [para sair digite 0]...\n",num);
            }
        }
        
        
        
        
        
    }
}
