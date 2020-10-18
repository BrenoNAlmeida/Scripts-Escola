/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/

// pessoas_50 : para a quantidade de pessoas maior de 50 anos 
// altura2 : para a soma das alturas das pessoas entre 10 e 20 anos
// media_a : para a media das alturas das pessoas entre 10 e 20
// pessoas2 : para a soma das pessoas menores de 40 anos
// po_pessoas : para porcentegem das pessoas inferios a 40 Kg

package lista2;

import java.util.Scanner;

public class Q8 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int idade;
        float altura, peso;
        // contadores
        int pessoas_50 = 0, pessoas_2 = 0, cont_p = 0;
        float altura2 = 0;
        //calculos da B e C
        float media_a, po_pessoas;
        // codigo operante
        for (int cont = 1; cont <= 25; cont++) {
            System.out.print("idade :");
            idade = sc.nextInt();
            System.out.print("altura :");
            altura = sc.nextFloat();
            System.out.print("peso : ");
            peso = sc.nextFloat();
            System.out.println("===========");
            //quantidade de pessoas maior de 50 anos
            if (idade > 50) {
                pessoas_50++;
            } 
            //total da altura de pessoas entre 10 e 20 anos
            else if (idade >= 10 && idade <= 20) {
                altura2 += altura;
                cont_p++;
            } 
            // total de pessoas com peso menos que 40 Kg
            else if (peso < 40) {
                pessoas_2++;
            }
        }
        // calculo media do peso das pessoas com idade entre 10 e 20 anos
        media_a = altura2 / cont_p;
        // calculo da porcentegem das pessoas com peso menor que 40 Kg referente ao total de pessoas  
        po_pessoas = (pessoas_2 * 100) / 25;
        // prints
        System.out.println("A quantidade de pessoas com idade superior a 50 anos : " + pessoas_50);
        System.out.println("A médias das alturas das pessoas com idade entre 10 e 20 anos : " + media_a);
        System.out.println("A porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas : " + po_pessoas);
    }
}
