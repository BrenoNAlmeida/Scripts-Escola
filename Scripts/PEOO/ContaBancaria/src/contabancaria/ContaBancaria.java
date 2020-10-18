package contabancaria;

import java.util.Scanner;

public class ContaBancaria {

    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
        Corrente[] VariasContas = new Corrente[100];
        Corrente conta;
        int escolha = 0;
        int posição = 0;
        System.out.println("-----crie sua primeira conta-----");
        System.out.println("digite seu nome = ");
        String nome = leia.next();
        System.out.println("digite o numero da conta = ");
        int numero = leia.nextInt();
        conta = new Corrente(nome, numero);
        VariasContas[posição] = conta;
        posição++;
        while (escolha != 6) {
            System.out.println("1 - criar nova conta");
            System.out.println("2 - retirar extrato ");
            System.out.println("3 - realizar saque ");
            System.out.println("4 - realizar deposito");
            System.out.println("5 - consultar numero e nome da conta ");
            System.out.println("6 - sair do terminal");
            escolha = leia.nextInt();
            switch (escolha) {
                case 1:
                    
                    System.out.println("digite seu nome = ");
                    nome = leia.next();
                    System.out.println("digite o numero da conta = ");
                    numero = leia.nextInt();
                    conta = new Corrente(nome,numero);  
                    VariasContas[posição] = conta;
                    posição++;
                    break;
                case 2:
                    System.out.println(VariasContas[posição].getextrato());
                    break;
                case 3:
                    System.out.println("digite o valor que o senhor deseja retirar = ");
                    float valor = leia.nextFloat();
                    System.out.println(VariasContas[posição].setsacar(valor));
                    break;
                case 4:
                    System.out.println("digite o valor que o senhor deseja depositar = ");
                    float deposito = leia.nextFloat();
                    VariasContas[posição].setdeposito(deposito);
                    System.out.println("deposito realizado com sucesso");
                    break;
                case 5:
                    System.out.println(VariasContas[posição].getconsultar());
                    break;
                case 6:
                    break;
                default:
                    System.out.println("obrigado por utilizar os nossos serviços");
                    break;

            }

        }

    }

}
