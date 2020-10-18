
package lista3;

import java.util.Scanner;


public class Q4 {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int pri = 0, seg = 0, ter = 0, qua = 0, qui = 0;
        int vetor [] = new int [15];
        for (int cont = 0; cont < vetor.length; cont++) {
            System.out.print("idade = ");
            int idade = sc.nextInt();
            vetor [cont] = idade;
        }
        for (int c = 0; c < vetor.length;c++){
            if (vetor[c] <= 15) {
               pri++;
           } else if (vetor[c] > 15 && vetor[c] <= 30) {
               seg++;
           } else if (vetor[c] > 30 && vetor[c] <= 45) {
               ter++;
           } else if (vetor[c] > 45 && vetor[c] <= 60) {
               qua++;
           } else {
               qui++;
           }

        }
        System.out.printf(" a quantaidade de pessoas na preimeira fachetaria é %d \n"
                + " a quantaidade de pessoas na segunda fachetaria é %d \n"
                + "a quantaidade de pessoas na terceira fachetaria é %d \n  "
                + "a quantaidade de pessoas na quarta fachetaria é %d \n "
                + "a quantaidade de pessoas na quinta fachetaria é %d \n ", pri, seg, ter, qua, qui);
        float calc1 = (pri * 15) / 100;
        float calc2 = (qui * 15) / 100;
        System.out.printf(" a porcentagem da primeira fachetria em relação ao total é %.2f\n"
                + "a porcentagem da ultima fachetria em relação ao total é %.2f\n", calc1, calc2);

    }

}
