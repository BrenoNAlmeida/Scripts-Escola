/*
alunos : Breno Nascimento de Almeida
         Hudson Santos de Lima Leite
Turma : PJD 2M

*/


package lista1;

import java.util.Scanner;

public class Questão11 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float car, rua, mul;
        System.out.print("qual a velocidade do carro ? ");
        car = sc.nextFloat();
        System.out.print("qual a velocidade maxima da rua ? ");
        rua = sc.nextFloat();
        mul = car - rua;
        System.out.println(mul);
        if (mul < 0) {
            System.out.println("você esta limpo meu chapa");
        } else if (mul <= 10) {
            System.out.println("sua multa é de 50 reais");
        } else if (mul <= 30) {
            System.out.println("sua multa é de 100");
        } else if (mul > 30) {
            System.out.println("sua multa é de 300");
        }
    }

}
