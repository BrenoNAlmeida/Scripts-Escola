/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;


public class Q3 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner (System.in);
        int cont , n = sc.nextInt();
        for (cont = 1 ; cont < 11; cont++){
            int calc = n * cont;
            System.out.printf("%d X %d = %d \n",n , cont ,calc);
        }
        
        
        
    }
}
