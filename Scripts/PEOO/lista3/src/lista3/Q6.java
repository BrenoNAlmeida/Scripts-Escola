
package lista3;

import java.util.Scanner;


public class Q6 {
    public static void main(String[] args) {
        

        Scanner sc = new Scanner(System.in);
        float[] altura = new float[25];
        float[] peso = new float[25];
        float[] idade = new float[25];
        int peso_menor_40 = 0, peso_total = 0, pessoas_acima_50_anos = 0, total_altura_pessoas_idade_entre10e20 = 0, contador_Pessoas_idade_entra10e20 = 0, media_Alturas_pessoas_entre10e20 = 0;
        for (int cont = 0; cont <= 24; cont++) {
            System.out.print(" qual sua idade ? ");
            idade[cont] = sc.nextInt();
            System.out.print(" qual sua altura ? ");
            altura[cont] = sc.nextInt();
            System.out.print(" qual seu peso ? ");
            peso[cont] = sc.nextFloat();
            System.out.println("------------------");
            
            peso_total += peso[cont];
            if(peso[cont] < 40){
                peso_menor_40 += peso[cont];
            }
            
            if (idade[cont] > 50) {
                pessoas_acima_50_anos++;
            } 
            else if (idade[cont] >= 10 && idade[cont] <= 20) {
                total_altura_pessoas_idade_entre10e20 += altura[cont];
                contador_Pessoas_idade_entra10e20++;
            } 
        }
        media_Alturas_pessoas_entre10e20 = total_altura_pessoas_idade_entre10e20 / contador_Pessoas_idade_entra10e20;
        
        System.out.println("A quantidade de pessoas com idade superior a 50 anos : " + pessoas_acima_50_anos);
        System.out.println("A medias das alturas das pessoas com idade entre 10 e 20 anos : " + media_Alturas_pessoas_entre10e20);
        System.out.println("A porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas : " + (( peso_menor_40 / peso_total ) * 100));
    }
}

        
        
