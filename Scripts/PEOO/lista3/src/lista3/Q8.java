
package lista3;

import java.util.Scanner;


public class Q8 {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        //variaveis da analise
        int idade = 0;
        float peso [] = new float [20];
        float altura [] = new float [20];
        String olhos [] = new String[20];
        String cabelo [] = new String [20];
        // contadores
        int cont_qa = 0, soma_id = 0;
        int cont_qc = 0, cont_qd = 0;
        int cont_qb = 0;
        for (int cont = 0; cont <= 19; cont++) {
            System.out.print("digite sua idade : ");
            idade = sc.nextInt();
            System.out.print("digite seu peso : ");
            peso [cont] = sc.nextFloat();
            System.out.print("digite sua altura : ");
            altura [cont] = sc.nextFloat();
            System.out.println("=========================");
            System.out.print(" qual a cor dos seus olhos ? :\n"
                    + "[A] - para Azul\n"
                    + "[P] - para preto\n"
                    + "[V] - para verde\n"
                    + "[C] - para castanho\n"
                    + "digite o codigo da cor dos seus olhos = ");
            olhos [cont] = sc.next().toUpperCase();
            System.out.println("======================");
            System.out.println("qual a cor dos seus cabelos ?\n"
                    + "[P] - para preto\n"
                    + "[C] - para castanho\n"
                    + "[L] - para louros\n"
                    + "[R] - para Ruivos\n"
                    + "digite o codigo da cor dos seus cabelos = ");
            cabelo [cont] = sc.next().toUpperCase();
        }
        
        for (int ver1 = 0; ver1 <= 19;ver1++){
              if (idade > 50 && peso[ver1] < 60) {
                cont_qa++;
            } else if (altura[ver1] < 1.50) {
                soma_id += idade;
                cont_qb++;
            } else if ("A".equals(olhos[ver1])) {
                cont_qc++;
            } else if ("R".equals(cabelo[ver1]) && !"A".equals(olhos[ver1])) {
                cont_qd++;
            }
        
        }
   
        float calc_media = 0;
        if(soma_id != 0 && cont_qb != 0){
            calc_media = soma_id / cont_qb;}
        float calc_porc = (cont_qc * 100) / 20;
        System.out.println(" A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos : " + cont_qa);
        System.out.println(" A média das idades das pessoas com altura inferior a 1,50 : " + calc_media);
        System.out.println("A percentagem de pessoas com olhos azuis entre todas as pessoas analisadas : " + calc_porc);
        System.out.println("A quantidade de pessoas ruivas e que não possuem olhos azuis : " + cont_qd);

        
        
        
        
        
        }
    }

