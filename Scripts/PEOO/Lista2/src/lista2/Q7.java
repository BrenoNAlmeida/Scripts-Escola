/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;

public class Q7 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String op = "";
        float compras_av = 0, compras_ap = 0;
        float tot_av = 0, tot_ap = 0;
        for (int cont = 1; cont < 15; cont++) {
            System.out.print("[V] - para comprar a vista \n"
                    + "[P] - para comprar a prazo \n"
                    + "====================================\n"
                    + "digite o codigo da operação = ");
            op = sc.next();
            op = op.toUpperCase();
            switch (op) {
                case "V":
                    System.out.println("digite o valor da transação =");
                    compras_av = sc.nextFloat();
                    tot_av += compras_av;
                    break;
                case "P":
                    System.out.println("digite o valor da transação =");
                    compras_ap = sc.nextFloat();
                    tot_ap += compras_ap;
                    break;
            }
        }
        float total = tot_av + tot_ap;
        float prestaçao = tot_ap / 3;
        System.out.printf("a. O valor total das compras à vista: %.2f \n"
                + " O valor total das compras a prazo: %.2f \n"
                + " O valor total das compras efetuadas: %.2f \n"
                + "O valor da primeira prestação das compras a prazo: %.2f \n", tot_av, tot_ap, total, prestaçao);

    }
}
