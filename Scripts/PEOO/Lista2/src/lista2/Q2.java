/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;


public class Q2 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner (System.in);
        float n, cont ,calc = 0;
        n = sc.nextInt();
        for ( cont = 1; cont <= n; cont++){
            calc += 1 / cont;
        }
        System.out.println(calc);
    }
}
