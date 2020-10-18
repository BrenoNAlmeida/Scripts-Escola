
package lista3;

import java.util.Arrays;


public class Q9 {
    public static void main(String[] args) {
               int cont,add = 0;
       int lista [] = new int [91];
        for ( cont = 1000 ;cont <=2000; cont++ ){
            if (cont % 11 ==5){
                lista [add] = cont;
                add++;
            }
        }
        System.out.println(Arrays.toString(lista));
        
        
        
    }
}
