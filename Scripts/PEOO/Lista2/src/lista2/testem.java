
package lista2;

import java.util.Arrays;
import java.util.Scanner;

public class testem {
    public static void main(String[] args) {
        Scanner sc =new Scanner (System.in);
        int matriz [] [] = new int [2][2];
        for( int linha = 0;linha < 2;linha++){
        for(int coluna = 0; coluna < 2;coluna++){
            System.out.println("numero = ");
            matriz[linha][coluna] = sc.nextInt();
        }
        }
        System.out.println(matriz[2][0]);
    }
}
