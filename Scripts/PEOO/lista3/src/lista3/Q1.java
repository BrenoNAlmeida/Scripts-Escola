package lista3;

import java.util.Scanner;

public class Q1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cont, n = sc.nextInt();
        int vetor[] = new int[11];
        for (cont = 0; cont <= 10; cont++) {
            int calc = n * cont;
            vetor[cont] = calc;
        }
        for (int pas = 0; pas <= 10; pas++) {
            System.out.printf("%d X %d = %d \n", n, pas, vetor[pas]);
        }

    }

}
