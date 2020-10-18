
package aulaoo;


import java.util.Scanner;


public class AulaOO {

    
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
        int opcao = 0;		
        lampada lamp = new lampada();

        do {
                System.out.println("\n---------------------------------------------");
                System.out.println("------------------ LAMPADA ------------------");
                System.out.println("1 - Ligar");
                System.out.println("2 - Desligar");
                System.out.println("3 - Está ligada?");
                System.out.println("0 - SAIR");
                System.out.println("---------------------------------------------");
                System.out.print("Digite a opção desejada: ");
                opcao = sc.nextInt();
                if(opcao == 1) {
                        lamp.ligar();
                        System.out.println("VOCÊ LIGOU A LÂMPADA!");
                }
                else if (opcao == 2) {
                        lamp.desligar();
                        System.out.println("VOCÊ DESLIGOU A LÂMPADA!");
                }
                else if (opcao == 3) {
                        System.out.print("Estado da Lâmpada: ");
                        if(lamp.estaLigada())
                                System.out.println("LIGADA");
                        else
                                System.out.println("DESLIGADA");
                }
                else if (opcao != 0) {
                        System.out.println("Opção inválida! Tente novamente...");
                }

        }while(opcao != 0);

        System.out.println("---------------------------------------------");
        System.out.println("-------------- FIM DE PROGRAMA --------------");
        System.out.println("---------------------------------------------");
}

}
