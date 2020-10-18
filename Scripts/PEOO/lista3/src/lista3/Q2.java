package lista3;

import java.util.Scanner;

public class Q2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String Vnome[] = new String[15];
        float Vbonus[] = new float[15];
        for (int cont = 0; cont < Vbonus.length; cont++) {
            String nome;
            float valor;
            System.out.print("digite seu nome = ");
            nome = sc.next();
            System.out.printf("senhor(a) %s qual foi sua o valor da sua compra no ano passado  ? ", nome);
            valor = sc.nextFloat();
            System.out.println("------------------------------------------------------------------");
            Vnome[cont] = nome;
            if (valor <= 1000) {
                float bonus = (10 * valor) / 100;
                Vbonus[cont] = bonus;
            } else {
                float bonus = (15 * valor) / 100;
                Vbonus[cont] = bonus;
            }

        }
        for(int cont2 =0; cont2< Vnome.length;cont2++){
        System.out.printf("senhor(a) %s você acaba de receber um bônus"
                     + " no valor de %.2f para gastar em nossa loja\n",Vnome[cont2],Vbonus[cont2]);
            System.out.println("-------------------------------------------------------------------------");
        
        }
    }
}

