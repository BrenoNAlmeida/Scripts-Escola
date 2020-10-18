package coisas_extras;

import java.util.Scanner;

public class Q2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n1, num, calc;
        n1 = sc.nextFloat();
        num = Math.sqrt(n1);
        calc = num - (Math.round(num));
        if (calc != 0) {
            System.out.printf("%.2f não é quadrado perfeito", n1);
        } else {
            System.out.printf(" %.2f é quadrado perfeito ", n1);
        }

    }

}
