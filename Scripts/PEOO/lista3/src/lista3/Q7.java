
package lista3;

import java.util.Scanner;


public class Q7 {
    

     public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int[] idade = new int[7];
        float[] peso = new float[7];
        float[] peso_maior_que_90 = new float[7];
        int contador_Peso = 0;
        float total_idades = 0, media_idades;
        for (int cont = 0; cont <= 6 ; cont++){
            System.out.print("digite sua idade = ");
            idade[cont] = sc.nextInt();
            System.out.print("digite seu peso = ");
            peso[cont] = sc.nextFloat();
            System.out.println("--------------");
            if (peso[cont] > 90){
                contador_Peso++;
            } 
        }
        for (int elem = 0; elem < 6; elem ++){
            total_idades += idade[elem];
            
        }
        
        System.out.println("A quantidade de pessoas com mais de 90 quilos = \n"+contador_Peso);
        System.out.printf("A médias das idades das 7 pessoas = %.2f \n",total_idades / idade.length);
    }
}

