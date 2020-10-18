/*
2alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M
0
*/

package lista1;

import java.util.Scanner;

public class Questão5 {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        int dia, mes, ano;
        System.out.print("que dia você nasceu ? ");
        dia = n.nextInt();
        System.out.print("qual o mês que você nasceu ?");
        mes = n.nextInt();
        System.out.print("qual o ano que você nasceu ?");
        ano = n.nextInt();
        if (dia > 31 || mes > 12) {
            System.out.println("dias/mes invalidos");
        }
        if (mes == 3 && dia >= 20 || mes == 4 && dia < 20) {
            System.out.println("seu signo é Aries");
        } else if (mes == 4 && dia > 20 || mes == 5 && dia <= 20) {
            System.out.println("seu signo é touros ");
        } else if (mes == 5 && dia > 20 || mes == 6 && dia <= 21) {
            System.out.println("seu signo é gêmeos ");
        } else if (mes == 6 && dia > 21 || mes == 7 && dia <= 22) {
            System.out.println("seu signo é câncer ");
        } else if (mes == 7 && dia > 22 || mes == 8 && dia <= 22) {
            System.out.println("seu signo é lêao");
        } else if (mes == 8 && dia > 24 || mes == 9 && dia <= 23) {
            System.out.println("seu signo é virgem ");
        } else if (mes == 9 && dia > 24 || mes == 10 && dia <= 23) {
            System.out.println("seu signo é libra");
        } else if (mes == 10 && dia >= 24 || mes == 11 && dia <= 22) {
            System.out.println("seu signo é escorpião ");
        } else if (mes == 11 && dia >= 23 || mes == 12 && dia <= 21) {
            System.out.println("seu signo é sagitario");
        } else if (mes == 12 && dia >= 22 || mes == 1 && dia <= 20) {
            System.out.println("seu signo é capricornio");
        } else if (mes == 1 && dia > 20 || mes == 2 && dia <= 19) {
            System.out.println("seu signo é aquario");
        } else if (mes == 2 && dia >= 20 || mes == 3 && dia <= 20) {
            System.out.println("seu signo é peixes");
        } else {
            System.out.println("erro");
        }

    }
}
