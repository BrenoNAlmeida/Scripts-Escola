
package coisas_extras;

import java.util.Arrays;
import java.util.Scanner;


public class momo {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a [] =  {1,2,3,4,5};
        int b [] = new int [5];
        int  add = 0;
        for (int c = 4; c > -1 ; c--){
            b[add] = a[c];
            add++;
        }
        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(b));
        
        
    }
}
