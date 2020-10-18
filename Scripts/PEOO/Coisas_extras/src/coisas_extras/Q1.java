
package coisas_extras;
import java.util.Scanner;

public class Q1 {

   
    public static void main(String[] args) {
        Scanner sc  = new Scanner (System.in);
        int num, cont = 0, analise;
        System.out.print("numero : ");
        num = sc.nextInt();
        while (cont <= num){
        cont ++;
        analise = num % cont;
            if (cont == 1){
            System.out.printf("os divisores de %d são :",num);
            }
            if (analise == 0){
                System.out.print(cont+", ");
            }
            
        }
        

  
        
    }
    
}
