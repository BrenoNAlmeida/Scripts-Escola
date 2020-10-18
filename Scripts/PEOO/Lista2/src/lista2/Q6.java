/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;

public class Q6 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int pri = 0, seg = 0, ter = 0, qua = 0, qui = 0;
        for (int cont = 1; cont <= 15; cont++) {
            System.out.print("idade = ");
            int idade = sc.nextInt();
            if (idade <= 15) {
                pri++;
            } else if (idade > 15 && idade <= 30) {
                seg++;
            } else if (idade > 30 && idade <= 45) {
                ter++;
            } else if (idade > 45 && idade <= 60) {
                qua++;
            } else {
                qui++;
            }
        }
        System.out.printf(" a quantaidade de pessoas na preimeira fachetaria é %d \n"
                + " a quantidade de pessoas na segunda fachetaria é %d \n"
                + "a quantaidade de pessoas na terceira fachetaria é %d \n  "
                + "a quantaidade de pessoas na quarta fachetaria é %d \n "
                + "a quantaidade de pessoas na quinta fachetaria é %d \n ", pri, seg, ter, qua, qui);
        float calc1 = (pri * 100) / 15;
        float calc2 = (qui * 100) / 15;
        System.out.printf(" a porcentagem da primeira fachetria em relação ao total é %.3f\n"
                + "a porcentagem da ultima fachetria em relação ao total é %.3f\n", calc1, calc2);

    }

}
