/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/

//cont_p : contador das pessoas maiores de 90 anos
// tot_idade para a soma da idade das 7 pessoas 
// media_id para a media da idade das 7 pessoas
package lista2;

import java.util.Scanner;


public class Q9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int idade;
        float peso;
        // contador
        int cont_p = 0;
        //variaveis da B
        float tot_idade = 0, media_id;
        // codigo operante
        for (int cont = 1; cont <= 7 ; cont++){
            System.out.print("idade : ");
            idade = sc.nextInt();
            System.out.print("peso : ");
            peso = sc.nextFloat();
            System.out.println("========");
            // para pessoas maiores que 90 Kg
            if (peso > 90){
                cont_p++;
            tot_idade += idade;
        }
        media_id = tot_idade / 7;
        System.out.println("A quantidade de pessoas com mais de 90 quilos : "+cont_p);
        System.out.printf("A médias das idades das 7 pessoas : %.2f \n",media_id);
        
    }
    }
}
