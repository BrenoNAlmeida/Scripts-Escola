
package lista3;

import java.util.Scanner;

public class Q5 {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);  
        float[] compras_avista = new float[15];
        float[] compras_aprazo = new float[15];
        float total_avista = 0, total_aprazo = 0;
        String opcao = "";
        
        for (int cont = 0; cont < 14; cont++) {
            System.out.print("digite V para comprar a vista \n"
                    + "digite P para comprar a prazo \n"
                    + "====================================\n"
                    + "digite o codigo da operacao : ");
            opcao = sc.next();
            opcao = opcao.toUpperCase();
            
                if("V".equals(opcao)){
                    System.out.print("digite o valor da transacao : ");
                    compras_avista[cont] = sc.nextFloat();
                }
                else if ("P".equals(opcao)){
                    System.out.println("digite o valor da transacao : ");
                    compras_aprazo[cont] = sc.nextFloat();
                }
        }
        
        for(int elem = 0; elem < compras_avista.length; elem++){
            total_avista += compras_avista[elem];
        }
        
        for(int elem = 0; elem < compras_aprazo.length; elem++){
            total_aprazo += compras_aprazo[elem];
        }
        
        float total_compras = total_avista + total_aprazo;
        float valor_prestacao = total_aprazo / 3;
        System.out.printf("a. O valor total das compras a  vista: %.2f \n"
                + " O valor total das compras a prazo: %.2f \n"
                + " O valor total das compras efetuadas: %.2f \n"
                + "O valor da primeira prestacao das compras a prazo: %.2f \n", total_avista, total_aprazo, total_compras, valor_prestacao);

    }

}
        
        
        
        
