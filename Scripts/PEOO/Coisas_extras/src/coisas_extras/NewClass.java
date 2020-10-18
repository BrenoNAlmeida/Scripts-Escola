/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package coisas_extras;

import java.util.Scanner;

/**
 *
 * @author ASUS
 */
public class NewClass {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] v = new int[5];
        System.out.println("digite aqui 5 números");
        for (int c = 0; c <= 4; c++) {
            v[c] = sc.nextInt();
        }
        for (int n = 0; n <= 4; n++) {
            for (int j = 0; j <= 4; j++) {
                if (v[j] < v[j ++]) {
                    int aux = v[j];
                    v[j] = v[j + 1];
                    v[j + 1] = aux;
                }
            }
        }
        System.out.println("em ordem crescente\n");
        for (int o = 0; o <= 4; o++) {
            System.out.println(v[o]);
        }
    }
}

