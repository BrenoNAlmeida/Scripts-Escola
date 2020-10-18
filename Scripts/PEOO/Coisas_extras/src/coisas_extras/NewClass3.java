
package coisas_extras;

import java.util.Scanner;


public class NewClass3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int n = 0;
        int l = 1;
        while (n != 0){
            l = l* (-1);
            n++;
            if (l > 0){
                System.out.println(n);
            }
        }
        
        
    }
}
