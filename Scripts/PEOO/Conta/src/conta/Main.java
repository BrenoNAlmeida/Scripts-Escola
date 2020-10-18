package conta;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Conta> contas = new ArrayList<Conta>();
        int ord = -1;
        int ope1 = 0;
        Conta conta;
        while (ope1 != 7) {
            System.out.println(" 1 - nova conta\n 2 - saque\n 3 - deposito");
            System.out.println(" 4 - transferencia bancaria\n 5 - consultar saldo\n 6 - informaçoes da conta");
            System.out.print(" 7 - sair\n operação = ");
            ope1 = sc.nextInt();
            switch (ope1) {
                case 1:
                    ord++;
                    System.out.println("1 - conta poupança\n 2 - conta corrente");
                    int ope2 = sc.nextInt();
                    switch (ope2) {
                        case 1:
                            System.out.print("nome =");
                            String nome = sc.next();
                            System.out.print("numero da conta = ");
                            int numeroConta = sc.nextInt();
                            conta = new ContaPoupanca(nome, numeroConta);
                            contas.add(conta);
                            break;
                        case 2:
                            System.out.print("nome =");
                            nome = sc.next();
                            System.out.print("numero da conta = ");
                            numeroConta = sc.nextInt();
                            System.out.println("limite = ");
                            float limite = sc.nextFloat();
                            conta = new ContaCorrente(nome, numeroConta, limite);
                            contas.add(conta);
                            break;
                    }
                    break;
                case 2:
                    System.out.print("saque = ");
                    float saque = sc.nextFloat();
                    try {
                        if (contas.get(ord) instanceof ContaPoupanca) {
                            contas.get(ord).saque(saque);

                            break;
                        } else if (contas.get(ord) instanceof ContaCorrente) {
                            contas.get(ord).saque(saque);

                            break;
                        }
                    } catch (SaqueNaoRealizado exceçao) {
                        System.out.println(exceçao);
                        break;

                    }

                case 3:
                    System.out.print("deposito = ");
                    float deposito = sc.nextFloat();
                    contas.get(ord).deposito(deposito);
                    break;
                case 4:
                    System.out.print("numero da conta  do destinatario = ");
                    int numeroConta = sc.nextInt();
                    try {
                        for (int cont = 0; cont < contas.size(); cont++) {
                            if (contas.get(cont).numeroConta == numeroConta) {
                                System.out.print("transferencia = ");
                                float transferencia = sc.nextFloat();
                                Conta con = contas.get(cont);
                                contas.get(ord).transferencia(transferencia, con);
                                break;
                            }if(cont == contas.size() -1 &&contas.get(cont).numeroConta != numeroConta){
                                System.out.println("conta nao encontrada");
                                break;
                            }
                        }
                    } catch (TransferenciaNaoRealizada exceçao) {
                        System.out.println(exceçao);
                        break;
                    }
                    break;
                case 5:
                    System.out.println("saldo = " + contas.get(ord).getSaldo());
                    break;

                case 6:
                    System.out.println(contas.get(ord).Consultar_usuario());
                    break;
                case 7:
                    break;

            }
        }

    }
}
