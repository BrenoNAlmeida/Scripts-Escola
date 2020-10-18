/*Breno Nascimento de Almeida
Adna Rute de Oliveira Mota
                  PJD2M
*/
package lista2;

import java.util.Scanner;

public class Q10 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //variaveis da analisa
        int idade;
        float peso, altura;
        String olhos, cabelo;
        // contadores
        int cont_qa = 0, soma_id = 0;
        int cont_qc = 0, cont_qd = 0;
        int cont_qb = 1;
        for (int cont = 1; cont <= 1; cont++) {            
            System.out.print("digite sua idade : ");
            idade = sc.nextInt();
            System.out.print("digite seu peso : ");
            peso = sc.nextFloat();
            System.out.print("digite sua altura : ");
            altura = sc.nextFloat();
            System.out.println("=========================");
            System.out.print(" qual a cor dos seus olhos ? :\n"
                    + "[A] - para Azul\n"
                    + "[P] - para preto\n"
                    + "[V] - para verde\n"
                    + "[C] - para castanho\n"
                    + "digite o codigo da cor dos seus olhos = ");
            olhos = sc.next();
            System.out.println("======================");
            System.out.println("qual a cor dos seus cabelos ?\n"
                    + "[P] - para preto\n"
                    + "[C] - para castanho\n"
                    + "[L] - para louros\n"
                    + "[R] - para Ruivos\n"
                    + "digite o codigo da cor dos seus cabelos = ");
            cabelo = sc.next();
            if (idade > 50 && peso < 60) {
                cont_qa++;
            } else if (altura < 1.50) {
                soma_id += idade;
                cont_qb++;
            } else if ("A".equals(olhos)) {
                cont_qc++;
            } else if ("R".equals(cabelo) && !"A".equals(olhos)) {
                cont_qd++;
            }
        }
        float calc_media = soma_id / cont_qb;
        float calc_porc = (cont_qc * 100) / 20;
        System.out.println(" A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos : " + cont_qa);
        System.out.println(" A média das idades das pessoas com altura inferior a 1,50 : " + calc_media);
        System.out.println("A percentagem de pessoas com olhos azuis entre todas as pessoas analisadas : " + calc_porc);
        System.out.println("A quantidade de pessoas ruivas e que não possuem olhos azuis : " + cont_qd);

    }
}
