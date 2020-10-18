/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;


public class Q4 {
    public static void main(String[] args) {
     Scanner sc = new Scanner (System.in);
     for (int cont = 1 ; cont <= 15 ; cont++){
     String nome;
     float valor;
         System.out.print("digite seu nome = ");
         nome = sc.next();
         System.out.printf("senhor(a) %s qual foi sua o valor da sua compra no ano passado  ? ",nome);
         valor = sc.nextFloat();
         if (valor <= 1000){
         float bonus = (10*valor)/100;
             System.out.printf("senhor(a) %s você acaba de receber um bônus"
                     + " no valor de %.2f para gastar em nossa loja\n",nome,bonus);
         }
         else{
            float bonus = (15*valor)/100;
             System.out.printf("senhor(a) %s você acaba de receber um bônus"
                     + " no valor de %.2f para gastar em nossa loja\n",nome,bonus);
         }
         System.out.println("=================================================="
                 + "===========================================================");      
     
     }
     
     
     
     
    }
}
