/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;

public class Q5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int idade;
        int addma = 0;
        for (int cont = 1; cont < 11; cont++) {
            System.out.print("qual a sua idade ? ");
            idade = sc.nextInt();
            if (idade >= 18) {
                addma++;
            }

        }
        System.out.printf(" %d pessoas são maior de idade", addma);

    }

}
