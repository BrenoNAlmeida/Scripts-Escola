package agenda;

import java.util.Scanner;

public class Agenda {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Contato c1 = new Contato();
        Contato ag[] = new Contato[5];
        int op = 0;
        do {
            System.out.println("[1] = adicionar contato\n[2] = consultar agenda\n [3] = sair");
            System.out.println("-------------------------");
            op = sc.nextInt();
            int pas = 0;
            switch (op) {
                case 1:
                    c1.adicionar(sc.nextInt(), sc.next());
                    ag[pas] = c1;
                    pas++;
                    break;
                case 2:
                    for (int c = 0; c < ag.length; c++) {
                        System.out.println(ag[c]);
                    }

            }

        } while (op != 3);

    }

}
